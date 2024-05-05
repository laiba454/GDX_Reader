# hello.py

"""Simple Hello, World example with PyQt6."""

import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

print ("i have done step 1")
print ("#############################################################")


from PyQt6.QtWidgets import QPushButton

# hello.py
# ...

# 2. Create an instance of QApplication
app = QApplication([])
print ("i have done step 2")
print ("#############################################################")



# hello.py
# ...

# 3. Create your application's GUI
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)
print ("i have done step 3")
print ("#############################################################")


# hello.py
# ...

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())
print ("i have done step 4")
print ("#############################################################")

