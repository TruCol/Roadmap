"""List of cost model parameters."""


# pylint: disable=R0903
class Params:
    """List of cost-model parameters."""

    def __init__(
        self,
    ):
        # Specify the wages used in the activities of the Gantt chart.
        self.wages = {
            "blockchain_dev": 75 + 1,
            "front_end_dev": 40 + 1,
            "human_resources": 35 + 1,
        }
        # Bounties used to attract initial protocol users.
        self.bounty_subsidising = 100000

        # Buffer to take unknown costs into account.
        self.buffer = 100000
