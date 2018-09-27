from cx_Freeze import setup, Executable

base = None    

executables = [Executable("TropOSrun.py", base=base)]

packages = ["idna", "TropOSkml", "TropOScsv", "datetime", "os"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "TropOS Drive Converter",
    options = options,
    version = "1.1",
    description = 'Converts .txt to .kml and .csv',
    executables = executables
)
