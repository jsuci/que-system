from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from sys import argv


# Subclass of QMainWindow to customize application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Hello World")
        label_1 = QLabel("WELCOME")
        label_2 = QLabel("Hello World")

        label_1.setAlignment(Qt.AlignCenter)
        label_2.setAlignment(Qt.AlignLeft)

        layout = QVBoxLayout()
        layout.addWidget(label_1)
        layout.addWidget(label_2)

        self.setLayout(layout)


app = QApplication(argv)

window = MainWindow()
window.show()

# Start event loop
app.exec_()
