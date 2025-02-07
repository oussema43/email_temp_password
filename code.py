import sys
import random , string
from PyQt6.QtWidgets import QMessageBox
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets

def genpassword(nb : int , isuper : int ,ilower : int , inumber : int , ipunctuation : int) -> str:
    
    """
    give number letter , is upper letter , lower letter , digits , punctuation output string random 
    """
    
    if isuper == 0 and ilower == 0 and inumber == 0 and ipunctuation == 0:
        return None
    char_boo = ''
    if isuper == 1:
        char_boo += string.ascii_uppercase
    if ilower == 1:
        char_boo += string.ascii_lowercase
    if inumber == 1:
        char_boo += string.digits
    if ipunctuation == 1:
        char_boo += string.punctuation
    return ''.join(random.choices(char_boo, k=nb))

def generate_temp_mail():
    domains = ['@gmail.com', '@outlook.com', '@russ_aka.com']
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return username + random.choice(domains)

class TempMailApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("gui.ui", self)
        self.coe.clicked.connect(self.copy_email)
        self.cop.clicked.connect(self.copy_password)
        self.bt1.clicked.connect(self.generate_email)
        self.bt3.clicked.connect(self.save_email)
    
    def copy_email(self):
        email = self.le.text()
        if len(email) == 0:
            QMessageBox.warning(self, "Warning", "No email to copy")
            return
        QtWidgets.QApplication.clipboard().setText(email)
        QMessageBox.information(self, "Information", "Email copied")
        return
    def copy_password(self):
        password = self.pas.text()
        if len(password) == 0:
            QMessageBox.warning(self, "Warning", "No password to copy")
            return
        QtWidgets.QApplication.clipboard().setText(password)
        QMessageBox.information(self, "Information", "Password copied")
        return

            
    
    def generate_email(self):
        self.le.setText(generate_temp_mail())
        self.pas.setText(genpassword(10, 1, 1, 1, 1))
    
    def save_email(self):
        email = self.le.text()
        password = self.pas.text()
        if email and password:
            with open("fichier.txt", "a") as file:
                file.write(email + " : " + password + "\n")
            QMessageBox.information(self, "Information", "Email and password saved")
            return
        else:
            QMessageBox.warning(self, "Warning", "No email and password to save")
            return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TempMailApp()
    window.show()
    sys.exit(app.exec())
