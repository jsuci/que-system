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


class UserWindow(QMainWindow, Ui_UserMainWindow):

    def __init__(self):
        super(UserWindow, self).__init__()
        self.setupUi(self)
        self.count = 0
        self.pushButton.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        # Ticket counter increment
        self.count += 1

        # Create new QWidget instance
        self.window = QWidget()

        # Position QWidget relative to parent window
        self.window.resize(280, 160)
        mid_x = ((self.width() - self.window.width()) // 2)
        mid_y = ((self.height() - self.window.height()) // 2)
        self.window.move(self.mapToParent(QPoint(mid_x, mid_y - 30)))

        # Customizing QWidget window
        self.window.setWindowModality(2)
        self.window.setWindowFlags(Qt.WindowCloseButtonHint)
        self.window.setWindowTitle(f"Priority Ticket #: {self.count:04d}")
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
        label_1 = QLabel("Your Ticket #:")
        label_1.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        label_1.setFont(font_1)
        label_1.setStyleSheet(
            """
            QLabel {
                border: 0px solid black;
                font-size: 25px;
                color: rgb(45, 45, 45);
                margin: 30px 0px 0px 0px;
            }
            """
        )

        # Creating and customizing label_2
        label_2 = QLabel(f"{self.count:04d}")
        label_2.setFont(font_2)
        label_2.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        label_2.setStyleSheet(
            """
            QLabel {
                border: 0px solid black;
                font-size: 70px;
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

        # Display QWidget
        self.window.show()


def main():
    # Preparing the main window
    app = QApplication(argv)
    window = UserWindow()

    # Launching the main window
    window.show()

    # Prevent from closing
    app.exec_()


if __name__ == "__main__":
    main()
