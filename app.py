import os
import sys
from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtGui import QIcon
from project_creator import create_project


class ProjectManager(QObject):
    @pyqtSlot(str, str, str)
    def createProject(self, project_type, project_name, project_path):
        # Ta bort 'file:///' från början av project_path om den finns
        if project_path.startswith('file:///'):
            project_path = project_path[8:]

        # Omvandla sökvägen till en absolut sökväg
        project_path = os.path.abspath(project_path)

        # Bygg fullständig sökväg till projektet
        full_path = os.path.join(project_path, project_name)
        
        # Använd funktionen från din project_creator.py för att skapa projektet
        success = create_project(project_type, project_name, full_path)
        
        # Visa ett meddelande till användaren beroende på om projektet skapades eller inte
        if success:
            self.show_message_box("Projekt skapat", "Projektet har skapats framgångsrikt.")
        else:
            self.show_message_box("Fel", "Det uppstod ett fel vid skapandet av projektet.")

    # En funktion för att visa ett meddelande till användaren
    def show_message_box(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('app_icon.png'))

    # Sätt organisationens namn och domän för att spara inställningar
    app.setOrganizationName("testing")
    app.setOrganizationDomain("test.se")

    # Skapa en QML-applikationsmotor och en projektmanager-instans
    engine = QQmlApplicationEngine()
    project_manager = ProjectManager()

    # Exponera projektmanager-instansen till QML
    engine.rootContext().setContextProperty("projectManager", project_manager)

    # Ladda QML-filen
    engine.load(QUrl.fromLocalFile('main.qml'))

    # Kontrollera att motorn har laddat QML-filen korrekt
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())