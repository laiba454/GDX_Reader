# # h_layout.py

# """HPushButton("Left"))
# # layout.addWidget(QPushButton("Center"))
# # layout.addWidget(QPushButton("Right"))

# layout.addWidget(QPushButton("Top"))
# layout.addWidget(QPushButton("Center"))
# layout.addWidget(QPushButton("Bottom"))
# window.setLayout(layout)

# window.show()
# sys.exit(app.exec())
# rint("step 1")orizontal layout example."""

# import sys

# from PyQt6.QtWidgets import (
#     QApplication,
#     QHBoxLayout,
#     QPushButton,
#     QWidget,
# )

# app = QApplication([])
# window = QWidget()
# window.setWindowTitle("QHBoxLayout")

# layout = QHBoxLayout()
# # layout.addWidget(Q
# print("######################################################")


# _layout.py

# """Vertical layout example."""

# import sys

# from PyQt6.QtWidgets import (
#     QApplication,
#     QPushButton,
#     QVBoxLayout,
#     QWidget,
# )

# app = QApplication([])
# window = QWidget()
# window.setWindowTitle("QVBoxLayout")

# layout = QVBoxLayout()
# layout.addWidget(QPushButton("Top"))
# layout.addWidget(QPushButton("Center"))
# layout.addWidget(QPushButton("Bottom"))
# window.setLayout(layout)

# print("step 2")
# print("######################################################")


# window.show()
# sys.exit(app.exec())# v


# # g_layout.py

# """Grid layout example."""

# import sys

# from PyQt6.QtWidgets import (
#     QApplication,
#     QGridLayout,
#     QPushButton,
#     QWidget,
# )

# app = QApplication([])
# window = QWidget()
# window.setWindowTitle("QGridLayout")

# layout = QGridLayout()
# layout.addWidget(QPushButton("Button (0, 0)"), 0, 0)
# layout.addWidget(QPushButton("Button (0, 1)"), 0, 1)
# layout.addWidget(QPushButton("Button (0, 2)"), 0, 2)
# layout.addWidget(QPushButton("Button (1, 0)"), 1, 0)
# layout.addWidget(QPushButton("Button (1, 1)"), 1, 1)
# layout.addWidget(QPushButton("Button (1, 2)"), 1, 2)
# layout.addWidget(QPushButton("Button (2, 0)"), 2, 0)
# layout.addWidget(
#     QPushButton("Button (2, 1) + 2 Columns Span"), 2, 1, 1, 2
# )
# window.setLayout(layout)

# window.show()
# sys.exit(app.exec())





# # f_layout.py

# """Form layout example."""

# import sys

# from PyQt6.QtWidgets import (
#     QApplication,
#     QFormLayout,
#     QLineEdit,
#     QWidget,
# )

# app = QApplication([])
# window = QWidget()
# window.setWindowTitle("QFormLayout")

# layout = QFormLayout()
# layout.addRow("Name:", QLineEdit())
# layout.addRow("Age:", QLineEdit())
# layout.addRow("Job:", QLineEdit())
# layout.addRow("Hobbies:", QLineEdit())
# window.setLayout(layout)

# window.show()
# sys.exit(app.exec())








# # dialog.py

# """Dialog-style application."""

# import sys

# from PyQt6.QtWidgets import (
#     QApplication,
#     QDialog,
#     QDialogButtonBox,
#     QFormLayout,
#     QLineEdit,
#     QVBoxLayout,
# )

# class Window(QDialog):
#     def __init__(self):
#         super().__init__(parent=None)
#         self.setWindowTitle("QDialog")
#         dialogLayout = QVBoxLayout()
#         formLayout = QFormLayout()
#         formLayout.addRow("Name:", QLineEdit())
#         formLayout.addRow("Age:", QLineEdit())
#         formLayout.addRow("Job:", QLineEdit())
#         formLayout.addRow("Hobbies:", QLineEdit())
#         dialogLayout.addLayout(formLayout)
#         buttons = QDialogButtonBox()
#         buttons.setStandardButtons(
#             QDialogButtonBox.StandardButton.Cancel
#             | QDialogButtonBox.StandardButton.Ok
#         )
#         dialogLayout.addWidget(buttons)
#         self.setLayout(dialogLayout)

# if __name__ == "__main__":
#     app = QApplication([])
#     window = Window()
#     window.show()
#     sys.exit(app.exec())




# # main_window.py

# """Main window-style application."""

# import sys

# from PyQt6.QtWidgets import (
#     QApplication,
#     QLabel,
#     QMainWindow,
#     QStatusBar,
#     QToolBar,
# )

# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__(parent=None)
#         self.setWindowTitle("QMainWindow")
#         self.setCentralWidget(QLabel("I'm the Central Widget"))
#         self._createMenu()
#         self._createToolBar()
#         self._createStatusBar()

#     def _createMenu(self):
#         menu = self.menuBar().addMenu("&Menu")
#         menu.addAction("&Exit", self.close)

#     def _createToolBar(self):
#         tools = QToolBar()
#         tools.addAction("Exit", self.close)
#         self.addToolBar(tools)

#     def _createStatusBar(self):
#         status = QStatusBar()
#         status.showMessage("I'm the Status Bar")
#         self.setStatusBar(status)

# if __name__ == "__main__":
#     app = QApplication([])
#     window = Window()
#     window.show()
#     sys.exit(app.exec())






# widget.signal.connect(slot_function)


# signals_slots.py

# """Signals and slots example."""

# import sys

# from PyQt6.QtWidgets import (
#     QApplication,
#     QLabel,
#     QPushButton,
#     QVBoxLayout,
#     QWidget,
# )

# def greet():
#     if msgLabel.text():
#         msgLabel.setText("")
#     else:
#         msgLabel.setText("Hello, World!")

# app = QApplication([])
# window = QWidget()
# window.setWindowTitle("Signals and slots")
# layout = QVBoxLayout()

# button = QPushButton("Greet")
# button.clicked.connect(greet)

# layout.addWidget(button)
# msgLabel = QLabel("")
# layout.addWidget(msgLabel)
# window.setLayout(layout)
# window.show()
# sys.exit(app.exec())




# signals_slots.py
# ...

def greet(name):
    if msg.text():
        msg.setText("")
    else:
        msg.setText(f"Hello, {name}")

# ...
        

        # signals_slots.py

"""Signals and slots example."""

import sys
from functools import partial

# ...

button = QPushButton("Greet")
button.clicked.connect(partial(greet, "World!"))

# ...