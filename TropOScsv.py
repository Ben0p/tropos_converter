from datetime import datetime

'''
Input TropOS Drive results .txt
Converts to formatted .csv
Returns filename of .csv
'''

def convert(file_in):
    '''
    Input raw TropOS drive.txt
    Output formatted .csv
    '''

    # File name excluding extention
    file_name = file_in.split('.')[0]
    # Formatted date YYYYmmdd
    timestamp = datetime.now().strftime('%Y%m%d')
    # File out .csv with datestamp
    file_out = '{}-{}.csv'.format(timestamp, file_name)

    # Create output .csv
    with open(file_out, 'w') as fo:
        # Add Headers
        fo.write('Latitude,Longitude,Upstream\n')
        # Open input .txt
        with open(file_in, 'r') as fi:
                # Read each line
            for line in fi:
                # Split lines (whitespace)
                row_in = line.split()
                # Get 'cell' data
                lat = row_in[0]
                lon = row_in[1]
                up = row_in[2]
                # Make any throughput greater than 3 round down to 3
                if float(up)>3:
                    up = 3
                # Format output row
                row_out = '{0},{1},{2}'.format(lat,lon,up)
                # Write out the row (line)
                fo.write(row_out+'\n')
            
            # Close the file in
            fi.close
        # Close the file out
        fo.close
    return(file_out)





if __name__ == '__main__':
    file_in = 'CTO-BRA.txt'
    convert(file_in)

    
