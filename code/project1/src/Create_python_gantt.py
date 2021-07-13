# The bottom up model that computes the TAM and TSM
import random
import numpy as np

from .Activity import Activity


def create_python_gantt():
    #activity=Activity(description, duration,  children=None,color=None, parent=None,starts_at_child_nr_start=None,starts_at_child_nr_end=None)
    
    # parent
    activity=Activity(description, duration)
    # children
    activity=Activity(description, duration)
    

def addTwo(self, x):
    """adds two to the incoming integer and returns the result of the computation."""
    return x + 2
