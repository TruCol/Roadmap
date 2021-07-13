# The bottom up model that computes the TAM and TSM
import random
import numpy as np

from .Plot_to_tex import Plot_to_tex as plt_tex
from .Create_python_gantt import create_python_gantt


class Gantt:
    def __init__(self):
        self.start_line="@startgantt"
        self.project_start_date="2021/07-22"
        self.closed_days=["saturday","sunday"]
        self.parent=create_python_gantt()
        self.end_line="@endgantt"
        

    def addTwo(self, x):
        """adds two to the incoming integer and returns the result of the computation."""
        return x + 2
