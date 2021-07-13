# The bottom up model that computes the TAM and TSM
import random
import numpy as np

from .Activity import Activity


def create_python_gantt():
    #activity=Activity(description, duration,  children=None,colour=None, parent=None,starts_at_child_nr_start=None,starts_at_child_nr_end=None)
    
    # parent
    parent=Activity("description", 5, "L0C0", colour="DarkOrchid")
    # children
    child_one=Activity("child one description", 2, "L1C0", parent=parent)
    child_two=Activity("child two description", 2, "L0C1", parent=parent)
    # merge family
    parent.add_children([child_one,child_two])
    
    return parent
    
        
    
def addTwo(self, x):
    """adds two to the incoming integer and returns the result of the computation."""
    return x + 2
