# pip install plantuml

# to compile locally:
# export  PLANTUML_LIMIT_SIZE=8192
# java -jar plantuml.jar -verbose sequenceDiagram.txt

# To compile with server:
from plantuml import PlantUML
import os
from os.path import abspath
from shutil import copyfile

def compile_gantt_locally(relative_plant_uml_java_filepath):
    print(f'relative_plant_uml_java_filepath={relative_plant_uml_java_filepath}')
    if check_if_java_file_exists(relative_plant_uml_java_filepath):
        print('FOUND')
    pass
        
    #diagram_dir = "./Diagrams"
    ##directory = os.fsencode()
    #for file in os.listdir(diagram_dir):
    #  filename = os.fsdecode(file)
    #  if filename.endswith(".txt"):
    #    server.processes_file(abspath(f'./Diagrams/{filename}'))
    #  if filename.endswith(".uml"):
    #    server.processes_file(abspath(f'./Diagrams/{filename}'))
    #    
    #  if filename.endswith(".png"):
    #    copyfile(abspath(f'./Diagrams/{filename}'),abspath(f'./../../latex/researchplan/Images/{filename}'))
        
def check_if_java_file_exists(relative_filepath):
    if os.path.isfile(relative_filepath):
        return True
    else:
        raise Exception(f"File:{relative_filepath} is not accessible")