from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QLabel
from sys import argv


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(280, 200)
        self.button = QPushButton("Hello World")
        self.label = QLabel("Hello Baby :)")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)
        self.newWindow()

    def newWindow(self):
        self.count = 0
        self.window2 = QWidget()
        self.window2.setGeometry(450, 300, 530, 280)
        self.label2 = QLabel(f"Hello Window 2 {self.count}")

        self.window2.layout = QVBoxLayout()
        self.window2.layout.addWidget(self.label2)
        self.window2.setLayout(self.window2.layout)

        self.window2.show()

    def magic(self):
        self.count += 1
        self.label2.setText(f"Hello Window 2 {self.count}")


def main():
    app = QApplication(argv)

    window_a = MainWindow()
    window_a.show()

    app.exec_()


if __name__ == "__main__":
    main()
