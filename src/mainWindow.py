import os
import re

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLineEdit, QPushButton, QFileDialog, QVBoxLayout, QSpacerItem, QTextEdit, QLabel, QCheckBox, QSizePolicy

from src.objects import PatternError
from src.trackSplitter import splitTracks
from src.messageBoxes import show_error_box, show_message_box

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flac track splitter")

        # Create the file selector widget
        self.file_selector = FileSelector()

        # Create the pattern choice widget
        self.pattern_choice = PatternChoice()

        # Create the time codes edit widget
        self.time_codes_edit = QTextEdit()

        # Create the big button to split the file
        self.split_button = QPushButton("Split File")
        self.split_button.clicked.connect(self.split)

        # Create the options widgets
        self.delete_checkbox = QCheckBox("Delete original file after splitting")
        self.clean_space_checkbox = QCheckBox("Compact spaces in timecodes (recommended)")
        self.clean_space_checkbox.setChecked(True) 

        # Create a layout for the main window
        layout = QVBoxLayout()
        layout.addWidget(self.file_selector)
        layout.addWidget(self.pattern_choice)
        layout.addWidget(self.time_codes_edit)
        layout.addItem(QSpacerItem(10, 10))  # Add a spacer to push the button to the bottom
        layout.addWidget(self.split_button)
        layout.addWidget(self.delete_checkbox)
        layout.addWidget(self.clean_space_checkbox)
        layout.setSpacing(10)  # Set spacing to 0 to make widgets close to each other
        layout.setContentsMargins(10, 10, 10, 10)  # Set margins to 0

        # Set layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def split(self):
        pattern = self.pattern_choice.pattern_edit.text()
        mainFileLocation = self.file_selector.file_path_edit.text()
        timeCodes = self.time_codes_edit.toPlainText()
        if self.clean_space_checkbox.isChecked():
            timeCodes = re.sub(r"[ \t]+", " ", timeCodes)
        try:
            splitTracks(pattern, timeCodes, mainFileLocation)
            show_message_box("File split successfully")
        except PatternError as e:
            show_error_box("Pattern mismatch. \n" + str(e))
        except Exception as e:
            show_error_box("Something went wrong. Here is the internal error: \n" + str(e))
        if self.delete_checkbox.isChecked():
            try:
                os.remove(mainFileLocation)
            except Exception as e:
                show_error_box("Could not delete original file. Here is the internal error: \n" + str(e))

class FileSelector(QWidget):
    def __init__(self):
        super().__init__()

        # Create the layout for the widget
        layout = QHBoxLayout()

        # Create the line edit widget to display the selected file path
        self.file_path_edit = QLineEdit()
        self.file_path_edit.setReadOnly(True)  # Set the line edit as read-only

        # Create the button to open the file selection dialog
        self.select_file_button = QPushButton("Select File")
        self.select_file_button.clicked.connect(self.open_file_dialog)
        
        # Add the widgets to the layout
        layout.addWidget(self.select_file_button)
        layout.addWidget(self.file_path_edit)

        # Set the layout for the widget
        layout.setContentsMargins(0, 0, 0, 0)  # Set margins to 0
        self.setLayout(layout)

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName()
        self.file_path_edit.setText(file_path)

class PatternChoice(QWidget):
    def __init__(self):
        super().__init__()

        # Create the layout for the widget
        layout = QHBoxLayout()

        # Create a QLabel for the title
        title_label = QLabel("Pattern:")
        layout.addWidget(title_label)

        # Create the line edit widget to display the selected file path
        self.pattern_edit = QLineEdit("%mm:%ss %tt")  # Set default value to a frequently used pattern
        layout.setContentsMargins(0, 0, 0, 0)  # Set margins to 0
        layout.addWidget(self.pattern_edit)

        # Set the layout for the widget
        self.setLayout(layout)
