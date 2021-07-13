# The bottom up model that computes the TAM and TSM
import random
import numpy as np

from .Plot_to_tex import Plot_to_tex as plt_tex


class Activity:
    def __init__(self, description, duration,  children=None,color=None, parent=None,starts_at_child_nr_start=None,starts_at_child_nr_end=None):
        self.parent=parent
        self.children=children
        self.description=description
        self.tag=tag
        self.duration=duration
        if (is None self.parent):
            if (is None color):
                raise Exception("Parent activity needs a colour")
            self.colour=colour
        else:
            self.starts_at_child_nr_start=starts_at_child_nr_start
            self.starts_at_child_nr_end=starts_at_child_nr_end
            self.colour=parent.colour
            

    def addTwo(self, x):
        """adds two to the incoming integer and returns the result of the computation."""
        return x + 2
