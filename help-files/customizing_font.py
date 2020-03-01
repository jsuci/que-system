# Customize font of any text
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel

# Set your widget ex. QLabel, QWidget etc..
label_1 = QLabel("Hello World")

# Create a new QFont object and pass in the
# widget's property ex. label_1.font()
font_1 = QFont()
font_1.setLetterSpacing(QFont.AbsoluteSpacing, 2.0)

# You can now apply font properties like
# setWeight, setLetterSpacing etc...
label_1.setFont(font_1)
