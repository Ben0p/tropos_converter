import os


'''
Mine Systems TropOS drive csv to kml converter
Input a formatted .csv of the TropOS drive results
Generates a .kml
'''


def generate(csv_in):
    '''
    Generate a .kml from a formatted .csv
    csv_in is the input formatted .csv
    '''

    # Header of .kml
    header = (
        '<?xml version="1.0" encoding="utf-8" ?>'
        '<kml xmlns="http://www.opengis.net/kml/2.2">'
        '   <Document id="root_doc">'
    )

    # Ledgend of the colors for each throughput result
    ledgend = (
        '       <Folder><name>Legend - Upstream</name>'
        '           <Placemark>'
        '               <name>&lt;span style=&quot;color:#e600e6;&quot;&gt;&lt;b&gt;3.000&lt;/b&gt;&lt;/span&gt;</name>'
        '           </Placemark>'
        '           <Placemark>'
        '               <name>&lt;span style=&quot;color:#003ae6;&quot;&gt;&lt;b&gt;2.000&lt;/b&gt;&lt;/span&gt;</name>'
        '           </Placemark>'
        '           <Placemark>'
        '               <name>&lt;span style=&quot;color:#00e674;&quot;&gt;&lt;b&gt;1.000&lt;/b&gt;&lt;/span&gt;</name>'
        '           </Placemark>'
        '           <Placemark>'
        '               <name>&lt;span style=&quot;color:#ace600;&quot;&gt;&lt;b&gt;0.000&lt;/b&gt;&lt;/span&gt;</name>'
        '           </Placemark>'
        '           <Placemark>'
        '               <name>&lt;span style=&quot;color:#e60000;&quot;&gt;&lt;b&gt;-1.000&lt;/b&gt;&lt;/span&gt;</name>'
        '           </Placemark>'
        '       </Folder>'
    )

    # Name for the drive results folder
    name = (
        '       <Folder><name>Track - {}</name>'
    )

    # Placemark for each segment of the results
    placemark = (
        '           <Placemark>'
        '               <name>&lt;span style=&quot;color:{c}&quot;&gt;{r}&lt;/span&gt;</name>'
        '               <Style><LineStyle><color>{lc}</color><width>4</width></LineStyle><PolyStyle><fill>0</fill></PolyStyle></Style>'
        '               <LineString><coordinates>{lon1},{lat1} {lon2},{lat2}</coordinates></LineString>'
        '           </Placemark>'
    )

    # Closing out the .kml
    footer = (
        '       </Folder>'
        '   </Document>'
        '  </kml>'
    )

    # Colors for throughputs
    color = {
        '3':'#e600e6',
        '2':'#003ae6',
        '1':'#00e674',
        '0':'#ace600',
        '-1':'#e60000'
        }

    # Colors for the segments
    line_color = {
        '3':'ffe600e6',
        '2':'ff003ae6',
        '1':'ff00e674',
        '0':'fface600',
        '-1':'ffe60000'
        }

    # Get the filename only from absolute directory?
    csv_filename = os.path.basename(csv_in)
    # Get the filename without extension
    drive_name = os.path.splitext(csv_filename)[0]
    # Add .kml extension to the drive_name
    kml_name = drive_name+'.kml'

    # Start point counter
    count = 0

    # Create .kml file
    with open(kml_name, 'w') as kml:
        # Write the header and ledgend to file
        kml.write(header)
        kml.write(ledgend)
        # Set the name inside kml
        name = name.format(drive_name)
        kml.write(name)

        # Open csv file for read only
        with open(csv_in,'r') as f:
            # Read each line
            for row in f:
                # Split line with comma deliminator
                cell = row.split(',')
                
                # Skip the first line in csv containing header info
                if count == 0:
                    count += 1
                    continue

                # Generate start of first segment from first point
                if count == 1:
                    lat2 = cell[0]
                    lon2 = cell[1]
                # From second point onwards, start of segment is the end of last segment
                else:
                    lat2 = lat1
                    lon2 = lon1
                # Second point of segment
                lat1 = cell[0]
                lon1 = cell[1]
                
                # Convert upload connection rate to float
                up = float(cell[2])
                
                # Set segment colors based on upload connection rate
                if 3 <= up:
                    up = color['3']
                    lc = line_color['3']
                elif 2 <= up < 3:
                    up = color['2']
                    lc = line_color['2']
                elif 1 <= up < 2:
                    up = color['1']
                    lc = line_color['1']
                elif 0 <= up < 1:
                    up = color['0']
                    lc = line_color['0']
                elif up < 0:
                    up = color['-1']
                    lc = line_color['-1']

                # Insert values into the kml segment
                track = placemark.format(
                    c=up,
                    r=count,
                    lon1=lon1,
                    lat1=lat1,
                    lon2=lon2,
                    lat2=lat2,
                    lc=lc
                    )

                # Write segment to file      
                kml.write(track)
                # Increase count
                count += 1
            # Print total points
            print("Processed {} points".format(count))
            # Close csv file
            f.close
        # Write out the footer to kml
        kml.write(footer)
        # Close the kml
        kml.close



if __name__ == '__main__':
    csv_file = '20180914-CTO-BRA.csv'
    generate(csv_file)

    
