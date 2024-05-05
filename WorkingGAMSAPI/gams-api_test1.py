import gams #does not import this lib
from gams import GamsWorkspace
from gams import GamsEquation #does not import this lib at all
from gams import GamsDatabase #does not import this lib at all 



# Path to the GAMS system directory
gams_dir = "C:/GAMS/45/"

# Initializing the GAMS workspace
ws = GamsWorkspace(system_directory=gams_dir)

# Path to the GDX file
gdx_file_path = "C:/Users/TECHNIFI/Desktop/gdx_task/Results_E2M2s_2023_to_2023.gdx"

# Loading the GDX file
gdx_data = ws.add_database_from_gdx(gdx_file_path)


#Accessing symbol information from the GDX file
for symbol in gdx_data:
    #print(f"Symbol: {symbol.name}")
    #print(type(symbol))
    #equations.update(symbol)
    #print(equations)
    if symbol.name == "EQ_AnnualFuelUseUB":
    #if symbol.name == "EQ_DemandElec":
        this_eq = symbol
        print(f"Symbol: {symbol.name}")
        for values in this_eq:
            print(values)
            print(type(values))      # These values are objects of <class 'gams.control.database.GamsEquationRecord'>, 
                                    #  and i need to convert them to someother form, python dictionary or in excel file etc.







   #  if symbol.name == "EQ_CostCO2byPlant":
   #    this_eq2 = symbol
   #    print(f"Symbol: {symbol.name}")
   #    for values in this_eq2:
   #       print(values)




           # if symbol_name[:2].lower() == 'eq':

   #  for record in symbol:
   #      print(dir(symbol))
   #      print(record)


