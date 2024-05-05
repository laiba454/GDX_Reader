from gdx2py import GdxFile     # Need to add this since gdxpds needs it, its a dependency 
# also discussed in this issue      https://github.com/NREL/gdx-pandas/issues/66

import gdxpds          # Throws this error      AttributeError: module 'gdx2py' has no attribute 'par2list'

gdx_file = 'C:/Users/TECHNIFI/Desktop/gdx_task/Results_E2M2s_2023_to_2023.gdx'
dataframes = gdxpds.to_dataframes(gdx_file)
for symbol_name, df in dataframes.items():
    print(f"Doing work with {symbol_name}\n{df}.")