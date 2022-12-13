from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import QCoreApplication
import sys

import socket


class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.i = 0
        self.setWindowTitle("Le serveur de tchat")
        self.resize(750, 750)
        self.__serveur = QLineEdit("Serveur : ")
        self.__port = QLineEdit("Port : ")
        self.__nbclient = QLineEdit("nombre de client maximum : ")
        self.textEdit = QTextEdit()
        self.textEdit.setEnabled(False)


        self.btnPress1 = QPushButton("Démarrage du serveur")
        self.btnPress2 = QPushButton("quitter")

        layout = QVBoxLayout()


        layout.addWidget(self.__serveur)
        layout.addWidget(self.__port)
        layout.addWidget(self.__nbclient)
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)

        self.setLayout(layout)

        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)

    def btnPress1_Clicked(self):
        self.btnPress1.setText("Arrêt du serveur")


    def btnPress2_Clicked(self):
        QCoreApplication.exit(0)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_()) 