import numpy as np

from .Activity import Activity


def create_python_gantt():
    # activity=Activity(description, duration,  children=None,colour=None, parent=None,starts_at_child_nr_start=None,starts_at_child_nr_end=None)
    parents = []
    # parent one
    parent_one = Activity("description", duration=5, new_tag=0, colour="Green")
    # children
    child_one = Activity(
        "child one description", duration=2, new_tag=0, parent=parent_one
    )
    child_two = Activity(
        "child two description", duration=2, new_tag=1, parent=parent_one
    )
    # merge family
    parent_one.add_children([child_one, child_two])
    parents.append(parent_one)

    parent_two = Activity("description two", duration=5, new_tag=1, colour="DarkOrchid")
    # children
    child_one = Activity(
        "child one description two", duration=2, new_tag=0, parent=parent_two
    )
    child_two = Activity(
        "child two description two", duration=2, new_tag=1, parent=parent_two
    )
    # merge family
    parent_two.add_children([child_one, child_two])
    parents.append(parent_two)

    ## parent
    # protocol = Activity(description="Develop protocol", duration=150)
    # platform_eco = Activity(description="Platform & ecosystem", duration=120)
    # consultancy = Activity(description="Launch consultancy", duration=150)
    #
    #
    ## children
    # onchain = Activity(description="On-chain", duration=30, parent=protocol)
    # git = Activity(description="Git integration", duration=60, parent=protocol)
    # oracle_ci = Activity(description="Oracle and continuous integration", duration=60, parent=git)
    # security = Activity(description="Security & Robustness", duration=150, parent=protocol)
    #
    # api = Activity(description="API", duration=50, parent=platform_eco)
    # bounties = Activity(description="Subsidize bounties", duration=7, parent=platform_eco)
    # marketing_platf = Activity(description="Marketing platform", duration=30, parent=platform_eco)
    # partners = Activity(description="Approach new partners", duration=20, parent=consultancy)
    # marketing_cons = Activity(description="Marketing consultancy", duration=30, parent=consultancy)
    # regist_cons = Activity(description="Registrations/admin/legal", duration=60, parent=consultancy)

    return parents


def addTwo(self, x):
    """adds two to the incoming integer and returns the result of the computation."""
    return x + 2
