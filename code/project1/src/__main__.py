import os
from .Main import Main
from .Compile_gantt_locally import compile_gantt_locally

print(f"Hi, I'll be running the main code, and I'll let you know when I'm done.")
project_nr = 1
main = Main()

# compile the gantt chart locally
compile_gantt_locally(main.relative_src_filepath, main.plant_uml_java_filename)

# export the code to latex
main.export_code_to_latex(project_nr)

# compile the latex report
main.compile_latex_report(project_nr)

print(f"Done.")
