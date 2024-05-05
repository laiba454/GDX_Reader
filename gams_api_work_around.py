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
    















#Access and print symbol information from the GDX file
for symbol in gdx_data:
    
    #if symbol.name == "EQ_AnnualFuelUseUB":
    if symbol.name == "EQ_DemandElec":
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
        


