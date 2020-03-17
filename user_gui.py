from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QLabel,
    QPushButton
)
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont
from sys import argv


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.displayWindow()
        self.btn_a.clicked.connect(lambda x: self.onClickButton("clear"))
        self.btn_b.clicked.connect(lambda x: self.onClickButton("eval"))
        self.btn_c.clicked.connect(lambda x: self.onClickButton("add_drop"))
        self.btn_d.clicked.connect(lambda x: self.onClickButton("others"))
        self.count = 0

        with open("ticket.log", "w") as fi:
            fi.write("")

    def midpoint(self, obj_a, obj_b):
        x = (obj_a.width() // 2) - (obj_b.width() // 2)
        y = (obj_a.height() // 2) - (obj_b.height() // 2)

        return x, y

    def onClickButton(self, name):
        self.count += 1

        if name == "clear":
            code = "CL"
        elif name == "eval":
            code = "EV"
        elif name == "add_drop":
            code = "AD"
        else:
            code = "OT"

        self.ticket = f"{self.count:03d}{code}"
        self.popWindow(self.ticket)

        # Exporting ticket code
        with open("ticket.log", "a") as fo:
            fo.write(f"{self.ticket},{name}\n")

    def createButton(self, name, pos_y):
        btn = QPushButton(name, self)
        btn.setFixedSize(self.ui_width - 50, 50)
        btn.setCursor(Qt.PointingHandCursor)
        btn_x, btn_y = self.midpoint(self, btn)
        btn.move(btn_x, pos_y)
        btn.setStyleSheet(
            """
            QPushButton {
                background: rgba(211, 141, 0, 1);
                font-size: 20px;
                font-weight: normal;
                border-radius: 8px;
            }
            QPushButton::hover {
                background: rgba(255, 227, 15, 1);
            }
            """
        )

        return btn

    def popWindow(self, ticket):

        self.pw = QWidget()
        self.pw.setWindowModality(2)
        self.pw.setWindowFlags(Qt.WindowCloseButtonHint)
        self.pw.setFixedSize(250, 190)
        self.pw.setWindowTitle(f"Ticket Code: {ticket}")
        pw_x, pw_y = self.midpoint(self, self.pw)
        self.pw.move(self.mapToParent(QPoint(pw_x - 1, pw_y + 30)))
        self.pw.setStyleSheet(
            """
            QWidget {
                background: rgba(255, 255, 255, 1);
            }
            """
        )

        pw_label_a = QLabel("Your Ticket Code:", self.pw)
        pw_label_a.setFixedSize(173, 38)
        pw_lx, pw_ly = self.midpoint(self.pw, pw_label_a)
        pw_label_a.move(pw_lx, 30)
        pw_label_a.setStyleSheet(
            """
            QLabel {
                color: #333333;
                font-weight: bold;
                font-size: 20px;
            }
            """
        )

        pw_label_b = QLabel(f"{ticket}", self.pw)
        pw_label_b.setFixedSize(220, 60)
        pw_bx, pw_by = self.midpoint(self.pw, pw_label_b)
        pw_label_b.move(pw_bx, pw_by)
        pw_label_b.setFont(self.font_b)
        pw_label_b.setStyleSheet(
            """
            QLabel {
                color: #000000;
                font-weight: bold;
                font-size: 55px;
                border: 1px solid #ffffff;
            }
            """
        )

        self.pw.show()

    def displayWindow(self):
        self.ui_width = 320
        self.ui_height = 450
        self.move(180, 70)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setFixedSize(self.ui_width, self.ui_height)
        self.setWindowTitle("IT Chairman's Office Que System")
        self.setStyleSheet(
            """
            QWidget {
                background: rgba(0, 0, 72, 1);
            }
            """
        )

        self.font_a = QFont()
        self.font_a.setLetterSpacing(QFont.AbsoluteSpacing, 10)

        self.font_b = QFont()
        self.font_b.setLetterSpacing(QFont.AbsoluteSpacing, 3.0)

        label_a = QLabel("WELCOME", self)
        label_a.setGeometry(5, 10, self.ui_width, 40)
        label_a.setFont(self.font_a)
        label_a.setStyleSheet(
            """
            QLabel {
                qproperty-alignment: AlignCenter;
                color: #ffffff;
                font-size: 40px;
                font-weight: 600;
            }
            """
        )

        label_b = QLabel("Please select any\noption below", self)
        label_b.setGeometry(0, 70, self.ui_width, 60)
        label_b.setFont(self.font_b)
        label_b.setStyleSheet(
            """
            QLabel {
                qproperty-alignment: AlignCenter;
                color: #ffffff;
                font-size: 22px;
                font-weight: 400;
            }
            """
        )

        self.btn_a = self.createButton("Clearance", 150)
        self.btn_b = self.createButton("Evaluation", 215)
        self.btn_c = self.createButton("Adding / Dropping", 280)
        self.btn_d = self.createButton("Others", 345)


def main():
    app = QApplication(argv)

    main_window = MainWindow()
    main_window.show()

    app.exec_()


if __name__ == "__main__":
    main()
