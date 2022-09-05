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
    # parents.append(parent_one)

    parent_two = Activity(
        "description two", duration=5, new_tag=1, colour="DarkOrchid"
    )
    # children
    child_one = Activity(
        "child one description two", duration=2, new_tag=0, parent=parent_two
    )
    child_two = Activity(
        "child two description two", duration=2, new_tag=1, parent=parent_two
    )
    # merge family
    parent_two.add_children([child_one, child_two])
    # parents.append(parent_two)

    ## parent
    # parent one
    protocol = Activity(
        description="Develop protocol",
        duration=120,
        new_tag=0,
        colour="Green",
        hourly_wage=0,
    )
    # children
    onchain = Activity(
        description="On-chain: Solidty+VRF",
        duration=60,
        new_tag=0,
        parent=protocol,
        hourly_wage=75,
    )
    git_tellor = Activity(
        description="Git integration: Tellor",
        duration=90,
        new_tag=1,
        parent=protocol,
        starts_at_child_nr_start=0,
        hourly_wage=75,
    )
    git_chainlink = Activity(
        description="Git integration: Chainlink",
        duration=90,
        new_tag=2,
        parent=protocol,
        starts_at_child_nr_start=0,
        hourly_wage=75,
    )
    alt_chains = Activity(
        description="Alternative Chains",
        duration=90,
        new_tag=3,
        parent=protocol,
        starts_at_child_nr_start=0,
        hourly_wage=75,
    )

    # grandchildren
    ci = Activity(
        description="(Decentralised) Continuous integration",
        new_tag=0,
        duration=30,
        parent=git_chainlink,
    )
    # git_chainlink.add_children([ci])
    security = Activity(
        description="Security & Robustness",
        duration=60,
        new_tag=1,
        parent=git_chainlink,
    )
    # ci.add_children([security])

    # merge
    protocol.add_children(
        [onchain, git_tellor, git_chainlink, alt_chains, ci, security]
    )
    parents.append(protocol)

    # parent_two
    platform_eco = Activity(
        description="Platform & ecosystem",
        duration=120,
        new_tag=1,
        colour="DarkOrchid",
        starts_at_child_nr_start=0,
        hourly_wage=40,
    )
    # children
    website = Activity(
        description="Website", duration=50, new_tag=0, parent=platform_eco
    )
    marketing_platf = Activity(
        description="Marketing platform",
        duration=30,
        new_tag=1,
        parent=platform_eco,
    )
    bounties = Activity(
        description="Subsidize bounties",
        duration=10,
        new_tag=2,
        parent=platform_eco,
    )
    platform_buffer = Activity(
        description="Platform Planning Buffer",
        duration=30,
        new_tag=3,
        parent=platform_eco,
    )

    # Grandchildren
    api = Activity(description="API", duration=50, new_tag=0, parent=website)
    gui = Activity(
        description="GUI",
        duration=50,
        new_tag=1,
        parent=website,
        starts_at_child_nr_start=0,
    )
    forum = Activity(
        description="Forum",
        duration=10,
        new_tag=2,
        parent=website,
        starts_at_child_nr_start=0,
    )
    website.add_children([api, gui, forum])

    platform_eco.add_children(
        [website, marketing_platf, bounties, platform_buffer]
    )
    parents.append(platform_eco)

    # parent_three
    company = Activity(
        description="Launch company",
        duration=150,
        new_tag=2,
        colour="Yellow",
        starts_at_child_nr_start=0,
        hourly_wage=35,
    )
    # children
    partners = Activity(
        description="Qualitative partner research",
        duration=20,
        new_tag=0,
        parent=company,
    )
    organisation = Activity(
        description="Establish organisation",
        duration=80,
        new_tag=1,
        parent=company,
    )
    marketing_company = Activity(
        description="Marketing", duration=30, new_tag=2, parent=company
    )
    company_buffer = Activity(
        description="Organisation Planning Buffer ",
        duration=20,
        new_tag=3,
        parent=company,
    )

    # Grandchildren
    auditing = Activity(
        description="Auditing", duration=10, new_tag=0, parent=organisation
    )
    hiring = Activity(
        description="Hiring", duration=20, new_tag=1, parent=organisation
    )
    administration = Activity(
        description="Administration",
        duration=10,
        new_tag=2,
        parent=organisation,
    )
    legal = Activity(
        description="Legal", duration=20, new_tag=3, parent=organisation
    )
    financial = Activity(
        description="Financial", duration=20, new_tag=4, parent=organisation
    )
    organisation.add_children(
        [auditing, hiring, administration, legal, financial]
    )

    company.add_children(
        [partners, organisation, marketing_company, company_buffer]
    )
    parents.append(company)

    return parents


def addTwo(self, x):
    """adds two to the incoming integer and returns the result of the
    computation."""
    return x + 2
