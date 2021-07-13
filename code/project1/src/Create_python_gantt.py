import numpy as np

from .Activity import Activity


def create_python_gantt():
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
    #parents.append(parent_one)

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
    #parents.append(parent_two)

    ## parent
    # parent one
    protocol = Activity(description="<size:44>Develop protocol", duration=120, new_tag=0, colour="Green")
    # children
    #onchain = Activity(description="<height:44>On-chain", duration=30, new_tag=0, parent=protocol)
    #onchain = Activity(description="<padding:44>On-chain", duration=30, new_tag=0, parent=protocol)
    #onchain = Activity(description="<margin:44>On-chain", duration=30, new_tag=0, parent=protocol)
    onchain = Activity(description="<LineThickness:44>On-chain", duration=30, new_tag=0, parent=protocol)
    onchain = Activity(description="<LineStyle:44>On-chain", duration=30, new_tag=0, parent=protocol)
    git = Activity(description="Git integration", duration=60,  new_tag=1,parent=protocol)
    security = Activity(description="Security & Robustness", duration=60,  new_tag=2, parent=protocol)
    # grandchildren
    oracle_ci = Activity(description="Oracle and continuous integration",  new_tag=0, duration=30, parent=git)
    git.add_children([oracle_ci])
    
    # merge
    protocol.add_children([onchain,oracle_ci,security])
    parents.append(protocol)
    
    
    # parent_two
    platform_eco = Activity(description="Platform & ecosystem", duration=120, new_tag=1, colour="DarkOrchid")
    # children
    api = Activity(description="API", duration=50, new_tag=0, parent=platform_eco)
    bounties = Activity(description="Subsidize bounties", duration=7, new_tag=1, parent=platform_eco)
    marketing_platf = Activity(description="Marketing platform", duration=30, new_tag=2, parent=platform_eco)
    platform_eco.add_children([api,bounties,marketing_platf])
    parents.append(platform_eco)
    
    # parent_three
    consultancy = Activity(description="Launch consultancy", duration=150, new_tag=2, colour="Yellow")
    # children
    partners = Activity(description="Approach new partners", duration=20, new_tag=0, parent=consultancy)
    marketing_cons = Activity(description="Marketing consultancy", duration=30, new_tag=1, parent=consultancy)
    regist_cons = Activity(description="Registrations/admin/legal", duration=60, new_tag=2, parent=consultancy)
    consultancy.add_children([partners,marketing_cons,regist_cons])
    parents.append(consultancy)
    
    return parents


def addTwo(self, x):
    """adds two to the incoming integer and returns the result of the computation."""
    return x + 2
