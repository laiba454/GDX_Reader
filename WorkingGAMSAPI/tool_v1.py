import gams
from gams import GamsWorkspace
from gams import GamsEquation
from gams import GamsDatabase



# Path to the GAMS system directory
gams_dir = "C:/GAMS/45/"

# Initialize the GAMS workspace
ws = GamsWorkspace(system_directory=gams_dir)

# Path to your GDX file
gdx_file_path = "C:/Users/TECHNIFI/Desktop/gdx_task/Results_E2M2s_2023_to_2023.gdx"

# Load the GDX file
gdx_data = ws.add_database_from_gdx(gdx_file_path)


def print_all_symbols():
    for symbol in gdx_data:
        print(f"Symbol: {symbol.name}")
        #print(type(symbol))
    


def print_all_equations():
    for symbol in gdx_data:
        if symbol.name.startswith("EQ"):
            print(f"Symbol: {symbol.name}")

    





def make_dict(eq_entered):
    # Access and print symbol information from the GDX file
    for symbol in gdx_data:
        if symbol.name == eq_entered:
            this_eq = symbol
            print(f"Symbol: {symbol.name}")

            for values in this_eq:
                string = str(values)

                # Splitting the string by ':' to separate the label and pairs of label-value pairs
                label, pairs = string.split(':')

                # Splitting pairs by space to get individual label-value pairs
                pairs_list = pairs.split()

                # Initialize an empty dictionary to store label-value pairs
                data = {label.strip(): {}}

                # Loop through each label-value pair
                for pair in pairs_list:
                    # Splitting each pair by '=' to separate label and value
                    key, value = pair.split('=')
                    # Storing each label-value pair in the dictionary
                    data[label.strip()][key.strip()] = value.strip()

                # Extracting the dictionary values
                level = float(data[label.strip()]['level'])
                lower = float(data[label.strip()]['lower'])
                upper = float(data[label.strip()]['upper'])

                # Displaying relevant dictionary key and values
                print(f"Key: {label.strip()}")
                print(f"Values: {data[label.strip()]}")

                # Comparing levels with upper and lower values
                if lower <= level <= upper:
                    print("Pass")
                else:
                    print("Fail")


            




#eq_entered = "EQ_DemandElec"
#make_dict(eq_entered)

















from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLineEdit
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt

import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GDX Data Display")

        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.text_area = QTextEdit()
        self.input_box = QLineEdit()
        self.button1 = QPushButton("Print All Symbols")
        self.button2 = QPushButton("Print All Equations")
        self.button3 = QPushButton("Make Dictionary")

        self.button1.clicked.connect(self.print_all_symbols)
        self.button2.clicked.connect(self.print_all_equations)
        self.button3.clicked.connect(self.make_dict)

        layout.addWidget(self.text_area)
        layout.addWidget(self.input_box)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        self.setCentralWidget(central_widget)

    def print_all_symbols(self):
        self.text_area.clear()
        for symbol in gdx_data:
            self.text_area.append(f"Symbol: {symbol.name}")

    def print_all_equations(self):
        self.text_area.clear()
        for symbol in gdx_data:
            if symbol.name.startswith("EQ"):
                self.text_area.append(f"Symbol: {symbol.name}")

    def make_dict(self):
        self.text_area.clear()
        eq_entered = self.input_box.text()
        if eq_entered:
            for symbol in gdx_data:
                if symbol.name == eq_entered:
                    this_eq = symbol
                    self.text_area.append(f"Symbol: {symbol.name}")

                    for values in this_eq:
                        string = str(values)

                        label, pairs = string.split(':')
                        pairs_list = pairs.split()
                        data = {label.strip(): {}}

                        for pair in pairs_list:
                            key, value = pair.split('=')
                            data[label.strip()][key.strip()] = value.strip()

                        level = float(data[label.strip()]['level'])
                        lower = float(data[label.strip()]['lower'])
                        upper = float(data[label.strip()]['upper'])

                        self.text_area.append(f"Key: {label.strip()}")
                        self.text_area.append(f"Values: {data[label.strip()]}")

                        redColor = QColor(255, 0, 0)
                        blackColor = QColor(0, 0, 0)
                        greenColor = QColor(0,255,0)

                        if lower <= level <= upper:
                            self.text_area.setTextColor(greenColor)
                            self.text_area.append("Pass")
                            self.text_area.setTextColor(blackColor)
                        else:
                            self.text_area.setTextColor(redColor)
                            self.text_area.append("Fail")
                            self.text_area.setTextColor(blackColor)





def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
