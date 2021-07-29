import os
from .Main import Main
from .Compile_gantt_locally import compile_gantt_locally

print(f"Hi, I'll be running the main code, and I'll let you know when I'm done.")
project_nr = 1


main = Main()

# create gantt chart
main.create_gantt()

# compile the gantt chart locally
compile_gantt_locally(
    main.relative_src_filepath, main.plant_uml_java_filename, main.src_to_gantt_path
)

# export the code to latex
main.export_code_to_latex(project_nr)

# compile the latex report
main.compile_latex_report(project_nr)

print(f"Done.")
