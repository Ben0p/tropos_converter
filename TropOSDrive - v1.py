from datetime import datetime


class convertTropOS():

    def __init__(self, file):
        self.file = file
        self.name = file.split('.')[0]
        self.filein = open(self.file, 'r')

    def createCSV(self):
        timestamp = datetime.now().strftime('%Y%m%H%M%S')
        self.filename = '{}-{}.csv'.format(timestamp, self.name)
        self.csvfile = open(self.filename, 'w')
        self.csvfile.write('Latitude,Longitude,Upstream\n')
        
    def populateCSV(self):
        for line in self.filein:
            row_in = line.split()
            row_out = self.genRow(row_in)
            self.genCSV(row_out)
        self.filein.close
        self.csvfile.close

    def genRow(self, row_in):

        lat = row_in[0]
        lon = row_in[1]
        up = row_in[2]

        if float(up)>3:
            up = 3
        
        row = [lat, lon, up]
        row_out = '{0},{1},{2}'.format(lat,lon,up)
        return(row_out)

    def genCSV(self, row_out):
        
        self.csvfile.write(row_out+'\n')




if __name__ == '__main__':

    file = 'Long.txt'
    convert = convertTropOS(file)
    convert.createCSV()
    convert.populateCSV()
    
