"""Tests whether the Dynamic_diagrams directory in latex is created and deleted
successfully."""
import os
import unittest

from src.export_data.helper_dir_file_edit import (
    create_dir_relative_to_root_if_not_exists,
    delete_dir_relative_to_root_if_not_exists,
    dir_relative_to_root_exists,
)

# import testbook


class Test_main(unittest.TestCase):
    """Test object."""

    # Initialize test object
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.script_dir = self.get_script_dir()
        self.project_name = "roadmap"

    def get_script_dir(self):
        """returns the directory of this script regardless of from which level
        the code is executed."""
        return os.path.dirname(__file__)

    def test_dir_relative_to_root_is_created_and_deleted(self):
        """Tests whether the Dynamic_diagrams directory in latex is created and
        deleted successfully."""
        dynamic_diagram_dir_relative_to_root = (
            f"latex/{self.project_name}/Images/Diagrams/Dynamic_diagrams"
        )
        create_dir_relative_to_root_if_not_exists(
            dynamic_diagram_dir_relative_to_root
        )
        self.assertTrue(
            dir_relative_to_root_exists(dynamic_diagram_dir_relative_to_root)
        )

        # Cleanup after
        delete_dir_relative_to_root_if_not_exists(
            dynamic_diagram_dir_relative_to_root
        )
        self.assertFalse(
            dir_relative_to_root_exists(dynamic_diagram_dir_relative_to_root)
        )
