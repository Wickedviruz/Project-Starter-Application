import os
import re

# Skapa en funktion som skriver till filer
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def fill_template(template_path, values):
    with open(template_path, 'r') as file:
        qml_template_content = file.read()
    
    filled_template = qml_template_content.format(**values)
    return filled_template

# Skapa en funktion som skapar ett tkinter-projekt
def create_pyQT_project(base_path, project_name):
    # Ta bort ogiltiga tecken från projektets namn och ersätt med "_"
    project_name = re.sub(r'[\/:*?"<>|]', '_', project_name)
    project_path = os.path.join(base_path, project_name)

    # Kontrollera om projektet redan existerar
    if os.path.exists(project_path):
        return False
    
     # Skapa projektstruktur
    os.makedirs(project_path, exist_ok=True)

    # Skapa sökvägar till mallar
    pyQT_content = os.path.join(os.path.dirname(__file__), 'Templates', 'pyQT', 'pyqt_template.py')
    qml_template_path = os.path.join(os.path.dirname(__file__), 'Templates', 'pyQT', 'qml_template.qml')

    #configurations
    qml_values = {
    'title': project_name,
    'width': '800',
    'height': '600'
    }

    qml_content = fill_template(qml_template_path, qml_values)

    
     # Anropa funktionen write_file för att skapa och skriva till filer
    write_file(os.path.join(project_path, 'app.py'),pyQT_content)
    write_file(os.path.join(project_path, 'main.qml'),qml_content)
    
    return True