from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QComboBox
)

from PyQt5.QtCore import Qt, QRunnable, QThreadPool
from PyQt5.QtGui import QFont
from sys import argv


class Worker(QRunnable):
    '''
    Worker thread
    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def run(self):
        '''
        Your code goes in this function
        '''
        self.fn(*self.args, **self.kwargs)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.threadpool = QThreadPool()
        self.displayWindow()
        self.callWindow()

    def displayWindow(self):

        self.count = 0

        self.setWindowTitle("Next Ticket Window")
        self.setGeometry(520, 100, 550, 280)
        self.setStyleSheet(
            """
            QWidget {
                background: rgb(0, 0, 72);
            }
            """
        )

        self.font1 = QFont()
        self.font1.setLetterSpacing(QFont.AbsoluteSpacing, 1.3)
        self.font1.setPixelSize(20)

        self.label1 = QLabel("Ticket Code", self)
        self.label1.setFixedSize(150, 40)
        mid_x1 = (self.width() - self.label1.width()) // 2
        self.label1.move(mid_x1, 10)
        self.label1.setFont(self.font1)
        self.label1.setStyleSheet(
            """
            QLabel {
                color:  rgba(255, 255, 255, 1);
                border: 1px solid rgba(255, 255, 255, 0.0);
                font-weight: 700;
                }
            """
        )
        self.label1.setAlignment(Qt.AlignCenter)

        font2 = QFont()
        font2.setLetterSpacing(QFont.AbsoluteSpacing, 1.3)
        font2.setPixelSize(60)

        self.label2 = QLabel("--------", self)
        self.label2.setFixedSize(350, 100)
        mid_x2 = (self.width() - self.label2.width()) // 2
        self.label2.move(mid_x2, 50)
        self.label2.setFont(font2)
        self.label2.setStyleSheet(
            """
            QLabel {
                color:  rgb(0, 0, 0);
                background: rgba(211, 141, 0, 1);
                border-radius: 10px;
                font-weight: 900;
                }
            """
        )
        self.label2.setAlignment(Qt.AlignCenter)

        self.label3 = QLabel("Proceed inside for", self)
        self.label3.setFixedSize(220, 40)
        mid_x3 = (self.width() - self.label3.width()) // 2
        self.label3.move(mid_x3, 170)
        self.label3.setFont(self.font1)
        self.label3.setStyleSheet(
            """
            QLabel {
                color:  rgba(255, 255, 255, 1);
                border: 1px solid rgba(255, 255, 255, 0.0);
                font-weight: 700;
                }
            """
        )
        self.label3.setAlignment(Qt.AlignCenter)

        font3 = QFont()
        font3.setPixelSize(30)
        font3.setLetterSpacing(QFont.AbsoluteSpacing, 1.3)

        self.label4 = QLabel("##########", self)
        self.label4.setFixedSize(320, 40)
        mid_x4 = (self.width() - self.label4.width()) // 2
        self.label4.move(mid_x4, 200)
        self.label4.setFont(font3)
        self.label4.setStyleSheet(
            """
            QLabel {
                color:  rgba(211, 141, 0, 1);
                border: 1px solid rgba(255, 255, 255, 0.0);
                font-weight: 700;
                }
            """
        )
        self.label4.setAlignment(Qt.AlignCenter)

    def callWindow(self):
        self.w2 = QWidget()
        self.w2.setStyleSheet(
            """
            QWidget {
                background: rgb(0, 0, 72);
            }
            """
        )
        self.w2.setWindowTitle("Caller Window")
        self.w2.setGeometry(520, 420, 550, 150)

        self.call_button = QPushButton("Call Next Ticket", self.w2)
        self.call_button.setGeometry(130, 70, 350, 45)
        self.call_button.clicked.connect(self.onButtonClick)
        self.call_button.setFont(self.font1)
        self.call_button.setStyleSheet(
            """
            QPushButton {
                background: rgba(211, 141, 0, 1);
                border-radius: 10px;
                color: rgba(0, 0, 0, 1);
                font-weight: 700;
            }
            QPushButton:hover {
                background: rgba(255, 227, 15, 1);
            }
            """
        )
        mid_btn = (self.w2.width() - self.call_button.width()) // 2
        self.call_button.move(mid_btn, self.call_button.y())

        self.cb_label = QLabel("Set Priority", self.w2)
        self.cb_label.setFont(self.font1)
        self.cb_label.move(100, 40)
        self.cb_label.setStyleSheet(
            """
            QLabel {
                font-size: 17px;
                font-weight: 900;
                color: rgba(255, 255, 255, 1);
            }
            """
        )

        self.combo = QComboBox(self.w2)
        self.combo.addItems(["Default", "Clearance", "Evaluation"])
        self.combo.setGeometry(220, 40, 230, 23)

        self.combo.setStyleSheet(
            """
            QComboBox {
                color: rgba(0, 0, 0, 1);
                background: rgba(255, 255, 255, 1);
                font-size: 13px;
            }

            """
        )

        self.w2.show()

    def onButtonClick(self):
        worker = Worker(self.magic)
        self.threadpool.start(worker)

    def magic(self):
        self.tickets = []
        with open("ticket.log", "r") as fi:
            for entry in fi:
                if entry != "":
                    self.tickets.append(tuple(entry.strip().split(",")))

        self.ticket_len = len(self.tickets)

        if self.count != self.ticket_len:
            self.label2.setText(f"{self.tickets[self.count][0]}")
            self.setWindowTitle(
                f"Next Ticket Code: {self.tickets[self.count][0]}")

            if self.tickets[self.count][1] == "clear":
                self.label4.setText("Clearance")
            elif self.tickets[self.count][1] == "eval":
                self.label4.setText("Evaluation")
            elif self.tickets[self.count][1] == "add_drop":
                self.label4.setText("Adding / Dropping")
            else:
                self.label4.setText("Other concerns")

            self.count += 1


def main():
    app = QApplication(argv)
    app.setStyle("fusion")

    window_a = MainWindow()
    window_a.show()

    app.exec_()


if __name__ == "__main__":
    main()
