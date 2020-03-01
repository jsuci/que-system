from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget
)
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
        self.window = QWidget()
        self.window.setWindowFlags(Qt.WindowCloseButtonHint)
        self.window.setWindowTitle("hello world")
        self.window.setStyleSheet(
            """
            QWidget {
                background: rgb(255, 255, 255);
            }
            """
        )

        self.window.resize(280, 200)
        mid_x = ((self.width() - self.window.width()) // 2)
        mid_y = ((self.height() - self.window.height()) // 2)
        self.window.move(self.mapToParent(QPoint(mid_x, mid_y)))
        self.window.show()

        print(self.width(), self.window.width())


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
