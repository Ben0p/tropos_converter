import glob, os
import TropOScsv
import TropOSkml



dir_path = os.path.dirname(os.path.realpath(__file__))
file_in = 'Long.txt'
os.chdir(dir_path)
for file in glob.glob("*.txt"):
    print('Converting '+file)
    convert_csv = TropOScsv.convert(file)
    csv_file = convert_csv.createCSV()
    convert_csv.populateCSV()
    generate = TropOSkml.generate(csv_file)
    generate.kml()
