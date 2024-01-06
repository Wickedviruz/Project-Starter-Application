// main.qml
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Dialogs 1.3

ApplicationWindow {
    visible: true
    width: 360
    height: 400
    title: "Project Generator"
    color: "#121212"  // Dark background

    ColumnLayout {
        anchors.fill: parent
        spacing: 20
        anchors.margins: 20

        // Style the project type selector
        ComboBox {
            id: projectType
            model: ["Flask", "Tkinter", "Command Line"]
            Layout.fillWidth: true
            font.pixelSize: 16
            background: Rectangle {
                color: "#1F1F1F"
                radius: 5
            }
        }

        // Style the project name input
        TextField {
            id: projectName
            placeholderText: "Enter Project Name"
            Layout.fillWidth: true
            font.pixelSize: 16
            color: "white"
            background: Rectangle {
                color: "#1F1F1F"
                radius: 5
            }
        }

        // Style the project path input and button
        RowLayout {
            Layout.fillWidth: true

            TextField {
                id: projectPath
                placeholderText: "Project Path"
                Layout.fillWidth: true
                font.pixelSize: 16
                color: "white"
                background: Rectangle {
                    color: "#1F1F1F"
                    radius: 5
                }
            }

            Button {
                id: browseButton
                text: "..."
                Layout.preferredWidth: 40
                font.pixelSize: 16
                background: Rectangle {
                    color: "#1F1F1F"
                    radius: 5
                }
                onClicked: {
                    fileDialog.open()
                }
            }
        }

        // Style the create project button
        Button {
            id: createButton
            text: "Create Project"
            Layout.fillWidth: true
            font.pixelSize: 16
            background: Rectangle {
                color: "#2979FF"  // Highlight color
                radius: 5
            }
            onClicked: {
                projectManager.createProject(projectType.currentText, projectName.text, projectPath.text)
            }
        }
    }

    FileDialog {
    id: fileDialog
    selectFolder: true  // Configure to select folders
    onAccepted: {
        if (fileDialog.fileUrls.length > 0) {
            var selectedPath = fileDialog.fileUrls[0].toString();
            if (selectedPath.startsWith("file:///")) {
                selectedPath = selectedPath.substring(8);  // Ta bort "file:///"
                }
                projectPath.text = selectedPath;  // Uppdatera projektets sökväg
            }
        }
    }
}