import gdxpy as gp
import os

# The path to your GDX file
gdxpath = os.path.join('C:/GAMS/45', 'C:/Users/TECHNIFI/Desktop/gdx_task/', 'Results_E2M2s_2023_to_2023.gdx')
print("start--------------------------")
tdata = gp.GdxFile(gdxpath) # Unable to open the file, because the library is broken and not maintained
