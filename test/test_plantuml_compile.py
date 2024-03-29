"""Tests whether the PlantUML diagrams that are created using Python code are
actually created."""
import os
import unittest

from src.export_data.helper_dir_file_edit import (
    create_dir_relative_to_root_if_not_exists,
    delete_dir_relative_to_root_if_not_exists,
    dir_relative_to_root_exists,
)
from src.export_data.plantuml_compile import (
    compile_diagrams_in_dir_relative_to_root,
)

# pylint: disable=R0801
from src.export_data.plantuml_generate import (
    create_trivial_gantt,
    output_diagram_text_file,
)


class Test_main(unittest.TestCase):
    """Test object used to execute tests."""

    # Initialize test object
    def __init__(self, *args, **kwargs):
        """Initialises test object."""
        super().__init__(*args, **kwargs)
        self.script_dir = self.get_script_dir()
        self.project_name = "roadmap"

    def get_script_dir(self):
        """returns the directory of this script regardless of from which level
        the code is executed."""
        return os.path.dirname(__file__)

    def test_if_plantuml_file_is_outputted(self):
        """Tests if the PlantUML file is correctly created."""
        diagram_text_filename = "trivial_gantt.uml"
        diagram_image_filename = "trivial_gantt.png"
        dynamic_diagram_dir_relative_to_root = (
            f"code/{self.project_name}/src/Diagrams/Dynamic_diagrams"
        )
        diagram_text_filepath_relative_to_root = (
            f"{dynamic_diagram_dir_relative_to_root}/{diagram_text_filename}"
        )
        diagram_image_filepath_relative_to_root = (
            f"{dynamic_diagram_dir_relative_to_root}/{diagram_image_filename}"
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

        # Compile diagrams to images.
        await_compilation = True
        extension = ".uml"
        jar_path_relative_from_root = (
            f"code/{self.project_name}/src/plantuml.jar"
        )
        relative_input_dir_from_root = dynamic_diagram_dir_relative_to_root
        verbose = True
        compile_diagrams_in_dir_relative_to_root(
            await_compilation,
            extension,
            jar_path_relative_from_root,
            relative_input_dir_from_root,
            verbose,
        )

        # Assert file exist.
        self.assertTrue(
            os.path.exists(diagram_image_filepath_relative_to_root)
        )

        # Cleanup after
        delete_dir_relative_to_root_if_not_exists(
            dynamic_diagram_dir_relative_to_root
        )
        self.assertFalse(
            dir_relative_to_root_exists(dynamic_diagram_dir_relative_to_root)
        )
