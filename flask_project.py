import os
import re

# Skapa en funktion som skapar ett flask-projekt
def create_flask_project(base_path, project_name):
    # Ta bort ogiltiga tecken från projektets namn och ersätt med "_"
    project_name = re.sub(r'[\/:*?"<>|]', '_', project_name)
    project_path = os.path.join(base_path, project_name)

    # Kontrollera om projektet redan existerar
    if os.path.exists(project_path):
        return False
    
    # Skapa projektstruktur
    #os.makedirs(project_path, exist_ok=True)
    
    # Skapa undermappar
    os.makedirs(os.path.join(project_path, 'app', 'templates'), exist_ok=True)
    os.makedirs(os.path.join(project_path, 'tests'), exist_ok=True)
    os.makedirs(os.path.join(project_path, 'venv'), exist_ok=True)

    # Anropa funktionen write_file för att skapa och skriva till filer
    write_file(os.path.join(project_path, 'run.py'), "from app import app\nif __name__ == '__main__':\n    app.run(debug=True)")
    write_file(os.path.join(project_path, 'requirements.txt'), "Flask\nFlask-SQLAlchemy\nFlask-Migrate")
    write_file(os.path.join(project_path, 'config.py'), "class Config(object)\ndebug = False\nTESTING = False\nDATABASTE_URI = 'sqldatabas'\nclass ProductionConfig(Config):\nDATABASE_URI = 'sqldatabas'\nclass DevelopmentConfig(Config):\nDEBUG = True\nclass TestingConfig(Config):\nTESTING = True")
    write_file(os.path.join(project_path, 'error.py'), "from app import app\nfrom flask import render_template\n@app.errorhandler(404)\ndef not_found_error(error):\nreturn render_template('404.html'), 404\n@app.errorhandler(500)\ndef internal_error(error):\nreturn render_template('500.html'), 500")
    write_file(os.path.join(project_path, 'app', '__init__.py'), "from flask import Flask\napp = Flask(__name__)\nfrom app import routes")
    write_file(os.path.join(project_path, 'app', 'routes.py'), "from app import app\n@app.route('/')\n@app.route('/index')\ndef index():\nreturn 'Hello, World!'")
    write_file(os.path.join(project_path, 'app', 'models.py'), "from flask_sqlalchemy import SQLAlchemy\ndb = SQLAlchemy(app)")
    write_file(os.path.join(project_path, 'tests', '__init__.py'), "import os\nimport tempfile\nimport pytest\nfrom app import app\nfrom app import db\nwith app.app_context():\n    db.create_all()\n@pytest.fixture\ndef client():\n    db_fd, app.config['DATABASE'] = tempfile.mkstemp()\n    app.config['TESTING'] = True\n   with app.test_client() as client:\n        with app.app_context():\n            yield client\n\
        \nos.close(db_fd)\n    os.unlink(app.config['DATABASE'])")

    return True

# Skapa en funktion som skriver till filer
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)