from PyQt6.QtWidgets import QMessageBox

def show_error_box(message):
    error_box = QMessageBox()
    error_box.setIcon(QMessageBox.Icon.Critical)
    error_box.setWindowTitle("Error")
    error_box.setText(message)
    error_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    error_box.exec()

def show_message_box(message):
    error_box = QMessageBox()
    error_box.setIcon(QMessageBox.Icon.Information)  # Change the icon to Information
    error_box.setWindowTitle("Message")
    error_box.setText(message)
    error_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    error_box.exec()
