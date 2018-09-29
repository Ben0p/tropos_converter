import glob, os
import time
import TropOScsv
import TropOSkml



# Start timer
start_time = time.time()


# Get working directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# Change directory to working directory
os.chdir(dir_path)

# Get all files ending in .txt
for file in glob.glob("*.txt"):
    print('Converting '+file)
    csv_file = TropOScsv.convert(file)
    TropOSkml.generate(csv_file)

elapsed = time.time() - start_time
print("Completed in {0:.2f} seconds".format(elapsed))
input("Press enter to exit ;)")
