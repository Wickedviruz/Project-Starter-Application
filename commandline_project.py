import os
import re

# Skapa en funktion som skapar ett command line-projekt
def create_command_line_project(base_path, project_name):
    # Ta bort ogiltiga tecken från projektets namn och ersätt med "_"
    project_name = re.sub(r'[\/:*?"<>|]', '_', project_name)
    project_path = os.path.join(base_path, project_name)

    # Kontrollera om projektet redan existerar
    if os.path.exists(project_path):
        return False
    
     # Skapa projektstruktur
    os.makedirs(project_path, exist_ok=True)
    
    # Anropa funktionen write_file för att skapa och skriva till filer
    write_file(os.path.join(project_path, 'run.py'),"import sys\nprint(sys.argv)")
    
    return True

# Skapa en funktion som skriver till filer
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)