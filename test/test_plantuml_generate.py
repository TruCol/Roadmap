"""Tests whether PlantUML .uml files are created correctly."""
import os
import unittest

from src.export_data.helper_dir_file_edit import (
    create_dir_relative_to_root_if_not_exists,
    delete_dir_relative_to_root_if_not_exists,
    dir_relative_to_root_exists,
)
from src.export_data.plantuml_generate import (
    create_trivial_gantt,
    output_diagram_text_file,
)


# pylint: disable=R0801
class Test_main(unittest.TestCase):
    """Test object."""

    # Initialize test object
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.script_dir = self.get_script_dir()
        self.project_name = "Whitepaper"

    # returns the directory of this script regardless of from which level the
    # code is executed
    def get_script_dir(self):
        """returns the directory of this script regardless of from which level
        the code is executed."""
        return os.path.dirname(__file__)

    # pylint: disable=R0801
    def test_if_plantuml_file_is_outputted(self):
        """Tests whether the plantuml file for the code generated Gantts are
        created correctly."""
        diagram_text_filename = "trivial_gantt.uml"

        dynamic_diagram_dir_relative_to_root = (
            f"code/{self.project_name}/src/Diagrams/Dynamic_diagrams"
        )
        diagram_text_filepath_relative_to_root = (
            f"{dynamic_diagram_dir_relative_to_root}/{diagram_text_filename}"
        )

        create_dir_relative_to_root_if_not_exists(
            dynamic_diagram_dir_relative_to_root
        )
        self.assertTrue(
            dir_relative_to_root_exists(dynamic_diagram_dir_relative_to_root)
        )

        # Generate a PlantUML diagram.
        filename, lines = create_trivial_gantt(diagram_text_filename)
        output_diagram_text_file(
            filename, lines, dynamic_diagram_dir_relative_to_root
        )

        # Assert file exist.
        self.assertTrue(os.path.exists(diagram_text_filepath_relative_to_root))

        # TODO: Assert file content is correct.

        # Cleanup after
        delete_dir_relative_to_root_if_not_exists(
            dynamic_diagram_dir_relative_to_root
        )
        self.assertFalse(
            dir_relative_to_root_exists(dynamic_diagram_dir_relative_to_root)
        )
