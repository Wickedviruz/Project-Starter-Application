# Purpose: Skapar projektet beroende på vilken typ som valts
from flask_project import create_flask_project
from tkinter_project import create_tkinter_project
from commandline_project import create_command_line_project
from pyQT_project import create_pyQT_project

def create_project(project_type, project_name, project_path):
    if project_type == 'Flask':
        return create_flask_project(project_path, project_name)
    elif project_type == 'Tkinter':
        return create_tkinter_project(project_path, project_name)
    elif project_type == 'PyQT':
        return create_pyQT_project(project_path, project_name)
    elif project_type == 'Command Line':
        return create_command_line_project(project_path, project_name)
    else:
        print("Okänd projekttyp")
        return False