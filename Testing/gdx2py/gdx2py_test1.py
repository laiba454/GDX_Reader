from gdx2py import GdxFile, GAMSSet, GAMSScalar, GAMSParameter
import pandas

# path to the GDX file
gdx_file = GdxFile('C:/Users/TECHNIFI/Desktop/gdx_task/Results_E2M2s_2023_to_2023.gdx')

print("######################################################")

#help(GdxFile)

# Printing all symbols in the GDX file
#for symbol_name in gdx_file.keys():
#    print(symbol_name)
#    print(type(gdx_file))


# Accessing a specific symbol from the GDX file
#symbol_name = 'ModelTime'
#symbol_data = gdx_file[symbol_name]
# Accessing data from the symbol


#for record in symbol_data:
#   print(record)
   #print(type(record))



######################################Equations not accesable ########################################
# Accessing equations from the GDX file
equation_name = 'EQ_CostFuel'  # The name of the equation you want to access
set2 = gdx_file['EQ_CostFuel']
print("The type of object when the equation is read is below")
print(type(set2))   # Returns none type ! cannot read equations
print(" ")
#set2 = gdx_file['EQ_CO2']  # Read a symbol
#gh = set2.to_pandas(gdx_file) # cannot find method to_pandas
#print(set2.values())


###################################### Parameters are accesible ########################################
# Can print the values and keys of the parameters 
set1 = gdx_file['DemandElec']  # Read a symbol
print(set1.values())
print(type(set1))
#pd = set1.to_pandas()
#print(type(pd))
#print(pd.keys())


##################################### Sets are accesible ##################################################
# values and keys method does not work
sym3 = gdx_file['Fuel']  # Read a symbol
#print(sym3.value)  # Throws this error " AttributeError: 'GAMSSet' object has no attribute 'value' "

for value in sym3:
    print(value)
    print("set above")
    
