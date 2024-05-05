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

    



eq_entered = "EQ_DemandElec"


def make_dict(eq_entered):
    #Access and print symbol information from the GDX file
    for symbol in gdx_data:
        #if symbol.name == "EQ_AnnualFuelUseUB":
        if symbol.name == eq_entered:
            this_eq = symbol
            print(f"Symbol: {symbol.name}")
            
            for values in this_eq:
                string = str(values)
                #print(string)
                # print("###################################################")

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

                # Printing the stored data
                #print(data)
                print(data.keys())
                print(type(data))
                print(data.values())
            
















from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit
import sys

# Replace the gdx_data with your actual data source here or pass it as an argument to the class
# Example:
# gdx_data = your_actual_gdx_data

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GDX Data Display")

        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.text_area = QTextEdit()
        self.button1 = QPushButton("Print All Symbols")
        self.button2 = QPushButton("Print All Equations")

        self.button1.clicked.connect(self.print_all_symbols)
        self.button2.clicked.connect(self.print_all_equations)

        layout.addWidget(self.text_area)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

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

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
