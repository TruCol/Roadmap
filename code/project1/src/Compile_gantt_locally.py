# pip install plantuml

# to compile locally:
# export  PLANTUML_LIMIT_SIZE=8192
# java -jar plantuml.jar -verbose sequenceDiagram.txt

# To compile with server:
from plantuml import PlantUML
import os
import subprocess
from os.path import abspath
from shutil import copyfile
import requests


def compile_gantt_locally(
    relative_src_filepath, plant_uml_java_filename, src_to_gantt_path
):
    relative_plant_uml_java_filepath = (
        f"{relative_src_filepath}{plant_uml_java_filename}"
    )
    print(f"relative_plant_uml_java_filepath={relative_plant_uml_java_filepath}")
    if got_java_file(relative_plant_uml_java_filepath):
        print("FOUND")
        os.environ["PLANTUML_LIMIT_SIZE"] = "8192"
        run_bash_command(
            f"java -jar {relative_plant_uml_java_filepath} -verbose {relative_src_filepath}{src_to_gantt_path}"
        )
        # export_gantt_to_latex(filename)
    pass


def check_if_java_file_exists(relative_filepath):
    if os.path.isfile(relative_filepath):
        return True
    else:
        return False
        
def got_java_file(relative_filepath):
    # Check if the jar file exists, curl it if not.
    if not check_if_java_file_exists(relative_filepath):
        # The java file is not found, curl it
        request_file("https://sourceforge.net/projects/plantuml/files/plantuml.jar/download", relative_filepath)
    # Check if the jar file exists after curling it. Raise Exception if it is not found after curling.
    if not check_if_java_file_exists(relative_filepath):
        raise Exception(f"File:{relative_filepath} is not accessible")
    print(f'Got the Java file')
    return True

def request_file(url, output_filepath):
    import requests
    # Request the file in the url
    response = requests.get(url)
    with open(output_filepath, "wb") as f:
       f.write(response.content)

def run_bash_command(bashCommand):
    subprocess.Popen(bashCommand, shell=True)


def export_gantt_to_latex(filename):
    if filename.endswith(".png"):
        copyfile(
            abspath(f"./Diagrams/{filename}"),
            abspath(f"./../../latex/researchplan/Images/{filename}"),
        )