from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QPoint
from usermainwindow import Ui_UserMainWindow
from sys import argv


class MainWindow(QMainWindow, Ui_UserMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Styling MainWindow
        self.setupUi(self)
        self.setWindowTitle("IT Chairman's Ofc. Que System")
        te2_font = QFont()
        te2_font.setLetterSpacing(QFont.AbsoluteSpacing, 1.3)
        self.textEdit_2.setFont(te2_font)
        self.move(180, 70)
        # Current position of MainWindow
        # print(self.mapToGlobal(self.pos()))

        # pushButton functions
        self.count = 0
        self.pushButton.clicked.connect(
            lambda x: self.onButtonClick("clear"))
        self.pushButton_2.clicked.connect(
            lambda x: self.onButtonClick("eval"))
        self.pushButton_3.clicked.connect(
            lambda x: self.onButtonClick("add_drop"))
        self.pushButton_4.clicked.connect(
            lambda x: self.onButtonClick("others"))

        with open("ticket.log", "w") as fi:
            fi.write("")

        # print(self.x(), self.width(), self.y(), self.height())

    def onButtonClick(self, name):
        # Generate ticket code
        self.count += 1

        if name == "clear":
            code = "CL"
        elif name == "eval":
            code = "EV"
        elif name == "add_drop":
            code = "AD"
        else:
            code = "OT"

        ticket = f"{self.count:03d}{code}"

        # Create new QWidget instance
        self.window = QWidget()

        # Position PopUp QWidget relative to parent window
        self.window.resize(264, 230)
        mid_x = ((self.width() - self.window.width()) // 2)
        mid_y = ((self.height() - self.window.height()) // 2)
        self.window.move(self.mapToParent(QPoint(mid_x, mid_y + 60)))

        # Customizing QWidget window
        self.window.setWindowModality(2)
        self.window.setWindowFlags(Qt.WindowCloseButtonHint)
        self.window.setWindowTitle(
            f"Ticket Code: {ticket}")
        self.window.setStyleSheet(
            """
            QWidget {
                background: rgb(255, 255, 255);
            }
            """
        )

        # Add contents to new QWidget
        self.window.layout = QVBoxLayout()

        # New font object
        font_1 = QFont()
        font_1.setLetterSpacing(QFont.AbsoluteSpacing, 0.0)

        font_2 = QFont()
        font_2.setLetterSpacing(QFont.AbsoluteSpacing, 1.5)

        # Creating and customizing lable_1
        label_1 = QLabel("Your Ticket Code:")
        label_1.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        label_1.setFont(font_1)
        label_1.setStyleSheet(
            """
            QLabel {
                border: 0px solid black;
                font-size: 20px;
                color: rgb(65, 65, 65);
                margin: 30px 0px 0px 0px;
                font-weight: bold;
            }
            """
        )

        # Creating and customizing label_2
        label_2 = QLabel(f"{ticket}")
        label_2.setFont(font_2)
        label_2.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        label_2.setStyleSheet(
            """
            QLabel {
                border: 0px solid black;
                font-size: 50px;
                font-weight: 900;
                color: rgb(0, 0, 0);
                margin: 10px 0px 60px 0px;
            }
            """
        )
        # Add all labels to current QWidget layout
        self.window.layout.addWidget(label_1)
        self.window.layout.addWidget(label_2)
        self.window.setLayout(self.window.layout)

        # Exporting ticket code
        with open("ticket.log", "a") as fo:
            fo.write(f"{ticket},{name}\n")

        # Display QWidget
        self.window.show()


def main():
    # Preparing the main window
    app = QApplication(argv)
    window = MainWindow()

    # Launching the main window
    window.show()

    # Prevent from closing
    app.exec_()


if __name__ == "__main__":
    main()
