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
        self.combo.activated.connect(lambda x: self.priority(x))
        self.curr_prio = 0
        self.df_count = 0
        self.cl_count = 0
        self.called = []

    def displayWindow(self):

        self.setWindowTitle("Next Ticket Window")
        self.setGeometry(520, 100, 550, 260)
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
        self.w2.setGeometry(520, 400, 550, 150)

        # Call next button
        self.call_button = QPushButton("Call Next Ticket", self.w2)
        self.call_button.setGeometry(130, 50, 350, 45)
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

        # Dropdown menu
        self.cb_label = QLabel("Set Priority", self.w2)
        self.cb_label.setFont(self.font1)
        self.cb_label.move(100, 20)
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
        self.combo.addItems(["Default", "Clearance",
                             "Evaluation", "Adding - Dropping",
                             "Other Concerns"])

        self.combo.setGeometry(220, 20, 230, 23)

        self.combo.setStyleSheet(
            """
            QComboBox {
                color: rgba(0, 0, 0, 1);
                background: rgba(255, 255, 255, 1);
                font-size: 13px;
            }
            QComboBox::item {
                background: #ffffff;
                border-top: 1px solid #dddddd;
                height: 20px;
            }

            QComboBox::item::selected {
                background: rgba(200, 200, 200, 1);
            }

            QComboBox:on {
                background: green;
            }
            """
        )

        # Notification
        self.font2 = QFont()
        self.font2.setLetterSpacing(QFont.AbsoluteSpacing, 1.4)
        self.label_notif = QLabel(
            "* Ticket Status *", self.w2)
        self.label_notif.setFont(self.font2)
        self.label_notif.setFixedWidth(300)
        notif_x = (self.w2.width() // 2) - (self.label_notif.width() // 2)
        self.label_notif.move(notif_x, 100)
        self.label_notif.setAlignment(Qt.AlignCenter)
        self.label_notif.setStyleSheet(
            """
            QLabel {
                font-size: 10px;
                color: #ffffff;
            }
            """
        )

        self.w2.show()

    def onButtonClick(self):
        worker = Worker(self.magic)
        self.threadpool.start(worker)

    def priority(self, s):
        if s == 0:
            self.label_notif.setText("* Processing default tickets *")
        elif s == 1:
            self.label_notif.setText("* Processing clearance tickets *")

        self.curr_prio = s

    def showCurrentTicket(self, ticket):
        self.label2.setText(f"{ticket[0]}")
        self.setWindowTitle(
            f"Next Ticket Code: {ticket[0]}")

        if ticket[1] == "clear":
            self.label4.setText("Clearance")
        elif ticket[1] == "eval":
            self.label4.setText("Evaluation")
        elif ticket[1] == "add_drop":
            self.label4.setText("Adding / Dropping")
        else:
            self.label4.setText("Other concerns")

    def magic(self):

        # Generating list of tickets from file including new ones
        self.all_tickets = []

        with open("ticket.log", "r") as fi:
            for entry in fi:
                if entry != "":
                    self.all_tickets.append(tuple(entry.strip().split(",")))

        # self.all_tickets = self.all_tickets[self.df_count:]

        if len(self.all_tickets[self.df_count:]) != 0:
            if self.curr_prio == 0:
                if self.df_count not in self.called:

                    self.showCurrentTicket(self.all_tickets[self.df_count])
                    self.priority(0)
                else:
                    self.label_notif.setText(
                        f"* {self.all_tickets[self.df_count][0]} "
                        f"Already Called *"
                    )

                self.df_count += 1
                self.cl_count = 0

            elif self.curr_prio == 1:
                self.cl_tickets = [
                    x for x in self.all_tickets[self.df_count:]
                    if x[1] == "clear"]

                if self.cl_count != len(self.cl_tickets):
                    self.showCurrentTicket(self.cl_tickets[self.cl_count])
                    self.called.append(self.all_tickets.index(
                        self.cl_tickets[self.cl_count]))

                else:
                    self.label_notif.setText(
                        f"* Clearance tickets done. "
                        f"Processing default tickets. *"
                    )

                    self.curr_prio = 0

                self.cl_count += 1

        else:
            self.label_notif.setText("* All tickets are called *")


def main():
    app = QApplication(argv)
    app.setStyle("fusion")

    window_a = MainWindow()
    window_a.show()

    app.exec_()


if __name__ == "__main__":
    main()
