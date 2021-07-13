# The bottom up model that computes the TAM and TSM
import random
import numpy as np
import copy

from .Plot_to_tex import Plot_to_tex as plt_tex


class Activity:
    def __init__(
        self,
        description,
        duration,
        new_tag,
        colour=None,
        parent=None,
        starts_at_child_nr_start=None,
        starts_at_child_nr_end=None,
    ):
        self.parent = parent
        self.description = description
        self.duration = duration
        self.children = []

        if self.parent is None:
            if colour is None:
                raise Exception("Parent activity needs a colour")
            self.colour = colour
            self.tag = []
        else:
            self.starts_at_child_nr_start = starts_at_child_nr_start
            self.starts_at_child_nr_end = starts_at_child_nr_end
            self.colour = parent.colour
            self.tag = copy.deepcopy(self.parent.tag)
            # self.tag=self.parent.tag

        # create tag
        self.tag.append(new_tag)

    def add_children(self, children):
        self.children = children

    def get_tag(self):
        return "_".join(list(map(lambda x: str(x), self.tag)))

    def addTwo(self, x):
        """adds two to the incoming integer and returns the result of the computation."""
        return x + 2
