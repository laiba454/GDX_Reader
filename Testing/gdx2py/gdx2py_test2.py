from gdx2py import GdxFile, GAMSSet, GAMSScalar, GAMSParameter  #does not support GAMSEquation
import pandas

# path to the GDX file
gdx_file = GdxFile('C:/Users/TECHNIFI/Desktop/gdx_task/Results_E2M2s_2023_to_2023.gdx')

print("-----------------------------------------------------")

#help(GdxFile)

#Print all symbols in the GDX file
for symbol_name in gdx_file.keys():
   print(symbol_name)
   print(type(gdx_file))

   #print(gdx_file.value()) #error says no attribute value, cannot access values










# Accessing a specific symbol from the GDX file
#symbol_name = 'ModelTime'
#symbol_data = gdx_file[symbol_name]
# Accessing data from the symbol


#for record in symbol_data:
#   print(record)
   #print(type(record))


print("################################################")
# Accessing a parameter
set1 = gdx_file['EndHourLoop']  # Read a symbol
print(set1)
print(type(set1))
pd = set1.to_pandas()
print(type(pd))
print(pd.keys())


print("################################################")
# Accessing equations from the GDX file
set2 = gdx_file['EQ_CO2']  # Read a equation and it tells nothing
print(set2)
#gh = set2.to_pandas(gdx_file)
#print(set2.values())
