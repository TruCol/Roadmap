# The bottom up model that computes the TAM and TSM
import random
import numpy as np

from .Plot_to_tex import Plot_to_tex as plt_tex
from .Create_python_gantt import create_python_gantt


class Gantt:
    def __init__(self, filepath):
        self.start_line="@startgantt"
        self.project_start_date="2021/07-22"
        self.closed_days=["saturday","sunday"]
        self.parent=create_python_gantt()
        self.end_line="@endgantt"
        self.lines=self.get_list()
        self.write_gantt(filepath,self.lines)
        
    def get_list(self):
        lines=[]
        lines.append(self.start_line)
        lines.append(f"project starts the {self.project_start_date}")
        lines=self.add_closed_dates(lines)
        #lines.append(f"[{parent.description}] as [{parent.tag}] lasts {parent.duration} days")
        lines = self.print_descriptions(self.parent, lines)
        lines = self.print_order(self.parent, lines)
        lines = self.print_colour(self.parent, lines)
        
        # TODO: specify order
        # TODO: specify colour
        lines.append(self.end_line)
        return lines
        
    def print_descriptions(self,activity, lines):
        lines.append("")
        lines.append(f"[{activity.description}] as [{activity.tag}] lasts {activity.duration} days")
        for child in activity.children:
            lines = self.print_descriptions(child, lines)
        return lines
        
    def print_order(self,activity, lines):
        lines.append("")
        
        # Write order for all children in an activity
        for i in range(0,len(activity.children)):
            if i == 0:
                lines.append(f"[{activity.children[i].tag}] starts at [{activity.tag}]'s start")
            else:
                lines.append(f"[{activity.children[i].tag}] starts at [{activity.children[i-1].tag}]'s end")
            
        # start recursive loop to write order of each of the childeren
        for child in activity.children:
            lines = self.print_order(child, lines)
        return lines
    
    def print_colour(self,activity, lines):
        lines.append("")
        lines.append(f"[{activity.tag}]  is colored in {activity.colour}")
        for child in activity.children:
            lines = self.print_colour(child, lines)
        return lines
    
    def add_closed_dates(self, lines):
        for closed_day in self.closed_days:
            lines.append(f"{closed_day} are closed")
        return lines
        
    def write_gantt(self, filepath, list):
        with open(filepath, 'w') as f:
            for item in list:
                f.write("%s\n" % item)
        f.close()

    def addTwo(self, x):
        """adds two to the incoming integer and returns the result of the computation."""
        return x + 2
