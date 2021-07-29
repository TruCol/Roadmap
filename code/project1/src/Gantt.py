# The bottom up model that computes the TAM and TSM
import random
import numpy as np

from .Plot_to_tex import Plot_to_tex as plt_tex
from .Create_python_gantt import create_python_gantt


class Gantt:
    def __init__(self, filepath):
        self.start_line = "@startgantt"
        self.project_start_date = "2021/07-22"
        self.closed_days = ["saturday", "sunday"]
        self.gantt_font_size="skinparam classFontSize 100"
        self.box_font_size="30"
        
        #self.font_size="skinparam defaultFontSize  100"

        self.parents = create_python_gantt()
        self.end_line = "@endgantt"
        self.lines = self.get_list()
        self.write_gantt(filepath, self.lines)
        
        self.costs = None

    def get_list(self):
        lines = []
        lines.append(self.start_line)
        lines.append(f"project starts the {self.project_start_date}")
        lines = self.add_closed_dates(lines)
        lines.append(self.gantt_font_size)
        # lines.append(f"[{parent.description}] as [{parent.get_tag()}] lasts {parent.duration} days")
        # for parent in self.parents:
        lines = self.loop_through_parents_printing(lines)
        lines.append(self.end_line)
        return lines

    def loop_through_parents_printing(self, lines):
        # print descriptions
        for i in range(0, len(self.parents)):
            lines = self.print_parent_descriptions(lines, self.parents[i])

        # print order
        for i in range(0, len(self.parents)):
            if i > 0:
                if not self.parents[i].starts_at_child_nr_start is None:
                    #print(f'starting parent at:{self.parents[i].starts_at_child_nr_start}')
                    lines.append(
                        f"[{self.parents[i].get_tag()}] starts at [{self.parents[i].starts_at_child_nr_start}]'s start"
                    )
                else:
                    print(f'parent_descr={self.parents[i].description}, and starts at {self.parents[i].starts_at_child_nr_start} and  tag={self.parents[i].get_tag()}, writing end')
                    lines.append(
                        f"[{self.parents[i].get_tag()}] starts at [{self.parents[i-1].get_tag()}]'s end"
                    )
            lines = self.print_parent_order(lines, self.parents[i])

        # print colour
        for i in range(0, len(self.parents)):
            lines = self.print_parent_colour(lines, self.parents[i])
        
        # compute costs
        total_costs = 0
        for i in range(0, len(self.parents)):
            total_costs, lines = self.print_parent_costs(total_costs, lines, self.parents[i])
        return lines

    def print_parent_descriptions(self, lines, parent):
        lines.append("")
        lines = self.print_descriptions(parent, lines)
        return lines

    def print_parent_order(self, lines, parent):
        lines.append("")
        lines = self.print_order(parent, lines)
        return lines

    def print_parent_colour(self, lines, parent):
        lines.append("")
        lines = self.print_colour(parent, lines)
        lines.append("")
        return lines
        
    def print_parent_costs(self, total_costs, lines, parent):
        lines.append("")
        total_costs, lines = self.print_costs(total_costs, parent, lines)
        print(f'total_costs={total_costs}')
        lines.append("")
        return total_costs, lines

    def print_descriptions(self, activity, lines):
        
        if not activity.font_size is None:
            font_size = activity.font_size
        else:
            font_size=self.box_font_size
        lines.append(
            f"[<size:{font_size}>{activity.description}] as [{activity.get_tag()}] lasts {activity.duration} days"
        )
        for child in activity.children:
            lines = self.print_descriptions(child, lines)
        return lines

    def print_order(self, activity, lines):
        # Write order for all children in an activity
        for i in range(0, len(activity.children)):
            if i == 0:
                lines.append(
                    f"[{activity.children[i].get_tag()}] starts at [{activity.get_tag()}]'s start"
                )
            else:
                # check if it starts at the start or end of some activity
                if not activity.children[i].starts_at_child_nr_start is None:
                    #print(f'activity.description={activity.description}, appending at  {activity.children[i].starts_at_child_nr_start}s  start')
                    lines.append(
                        f"[{activity.children[i].get_tag()}] starts at [{activity.children[i].starts_at_child_nr_start}]'s start"
                    )
                else: 
                    #print(f'activity.description={activity.description}, appending at  {activity.children[i-1].get_tag()}s  end')
                    lines.append(
                        f"[{activity.children[i].get_tag()}] starts at [{activity.children[i-1].get_tag()}]'s end"
                    )

        # start recursive loop to write order of each of the childeren
        for child in activity.children:
            lines = self.print_order(child, lines)
        return lines

    def print_colour(self, activity, lines):
        lines.append(f"[{activity.get_tag()}]  is colored in {activity.colour}")
        for child in activity.children:
            lines = self.print_colour(child, lines)
        return lines
        
    def print_costs(self, total_costs, activity, lines):
        lines.append(f"'[{activity.description}]  takes: {activity.duration}[days] equating to:{activity.duration*activity.hours_per_day}[hours] and costs: {activity.hourly_wage} per hour, yielding activity costs: {activity.duration*activity.hours_per_day*activity.hourly_wage} Euros.")
        total_costs=total_costs+activity.duration*activity.hours_per_day*activity.hourly_wage
        for child in activity.children:
            total_costs, lines = self.print_costs(total_costs, child, lines)
        return total_costs, lines

    def add_closed_dates(self, lines):
        for closed_day in self.closed_days:
            lines.append(f"{closed_day} are closed")
        return lines

    def write_gantt(self, filepath, list):
        with open(filepath, "w") as f:
            for item in list:
                f.write("%s\n" % item)
        f.close()

    def addTwo(self, x):
        """adds two to the incoming integer and returns the result of the computation."""
        return x + 2
