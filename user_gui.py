from PyQt5 import QtWidgets
from user_gui_pyuic5 import Ui_UserMainWindow
from sys import argv


class UserWindow(QtWidgets.QMainWindow, Ui_UserMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        # # Fixed width
        # self.setMinimumWidth(320)
        # self.setMaximumWidth(320)

        # # Fix height
        # self.setMinimumHeight(480)
        # self.setMaximumHeight(480)

        # self.setTitle("Student Que System")


def main():
    # Preparing the window
    app = QtWidgets.QApplication(argv)
    window = UserWindow()

    # Launching the window
    window.show()

    # Prevent from closing
    app.exec_()


if __name__ == "__main__":
    main()
