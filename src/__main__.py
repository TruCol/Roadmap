"""Entry point for this project, runs the project code and exports data if
export commands are given to the cli command that invokes this script."""


from src.arg_parser import parse_cli_args
from src.export_data.export_data import export_data

# Project code imports.
from src.Gantt import Gantt

# Export data import.


# Parse command line interface arguments to determine what this script does.
args = parse_cli_args()

# create gantt chart
gantt = Gantt("src/export_data/Diagrams/Dynamic_diagrams/gantt.uml")

# Export Gantt to Latex
# main.export_gantt_to_latex()

# compile the gantt chart locally
# compile_gantt_locally(
#    main.relative_src_filepath, main.plant_uml_java_filename, main.src_to_gantt_path
# )

# Run data export code if any argument is given.
if not all(
    arg is None for arg in [args.l, args.dd, args.sd, args.c2l, args.ec2l]
):
    export_data(args)
