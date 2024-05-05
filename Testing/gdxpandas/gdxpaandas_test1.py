from gdxpds.gdx import GdxFile

# Load the GDX file
gdx_path = 'C:/Users/TECHNIFI/Desktop/gdx_task/Results_E2M2s_2023_to_2023.gdx'
gdx = GdxFile(gdx_path)

# List symbols available in the GDX file
print(gdx._symbols)

# Read a specific symbol from the GDX file and convert into a Pandas DataFrame, but it gives a key error 
data = gdx['DemandElec'].to_dataframe()
print(data)
