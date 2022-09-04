# File used to export data to latex.
from src.export_data.create_dynamic_diagrams import create_dynamic_diagrams
from src.export_data.create_static_diagrams import create_static_diagrams
from src.export_data.latex_compile import compile_latex
from src.export_data.latex_export_code import export_code_to_latex

from .Hardcoded_data import Hardcoded_data


def export_data(args):
    """Parses the Python arguments that specify what should be compiled.

    :param args:
    """

    hd = Hardcoded_data()

    # Generating PlantUML diagrams
    create_dynamic_diagrams(args, hd)
    create_static_diagrams(args, hd)

    # Plotting graphs using Python code, and export them to latex.
    # Generate plots.
    # Export plots to LaTex.

    # Export code to LaTex.
    if args.c2l:
        # TODO: verify whether the latex/{project_name}/Appendices folder
        # exists before exporting.
        # TODO: verify whether the latex/{project_name}/Images folder exists
        # before exporting.
        export_code_to_latex(hd, False)
    elif args.ec2l:
        # TODO: verify whether the latex/{project_name}/Appendices folder
        # exists before exporting.
        # TODO: verify whether the latex/{project_name}/Images folder exists
        # before exporting.
        export_code_to_latex(hd, True)

    # Compile the accompanying LaTex report.
    if args.l:
        compile_latex(True, True)
        print("")
    print("\n\nDone exporting data.")
