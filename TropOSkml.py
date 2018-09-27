import os


class generate():

    def __init__(self, csv):
    
        self.header ='''<?xml version="1.0" encoding="utf-8" ?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document id="root_doc">
'''

        self.ledgend = '''<Folder><name>Legend - Upstream</name>
  <Placemark>
	<name>&lt;span style=&quot;color:#e600e6;&quot;&gt;&lt;b&gt;3.000&lt;/b&gt;&lt;/span&gt;</name>
  </Placemark>
  <Placemark>
	<name>&lt;span style=&quot;color:#003ae6;&quot;&gt;&lt;b&gt;2.000&lt;/b&gt;&lt;/span&gt;</name>
  </Placemark>
  <Placemark>
	<name>&lt;span style=&quot;color:#00e674;&quot;&gt;&lt;b&gt;1.000&lt;/b&gt;&lt;/span&gt;</name>
  </Placemark>
  <Placemark>
	<name>&lt;span style=&quot;color:#ace600;&quot;&gt;&lt;b&gt;0.000&lt;/b&gt;&lt;/span&gt;</name>
  </Placemark>
  <Placemark>
	<name>&lt;span style=&quot;color:#e60000;&quot;&gt;&lt;b&gt;-1.000&lt;/b&gt;&lt;/span&gt;</name>
  </Placemark>
</Folder>
'''

        self.name = '''<Folder><name>Track - {}</name>
'''

        self.placemark = '''  <Placemark>
	<name>&lt;span style=&quot;color:{c}&quot;&gt;{r}&lt;/span&gt;</name>
	<Style><LineStyle><color>{lc}</color><width>4</width></LineStyle><PolyStyle><fill>0</fill></PolyStyle></Style>
      <LineString><coordinates>{lon1},{lat1} {lon2},{lat2}</coordinates></LineString>
  </Placemark>
'''

        self.footer = '''</Folder>
</Document></kml>
'''

        self.color = {'3':'#e600e6',
         '2':'#003ae6',
         '1':'#00e674',
         '0':'#ace600',
          '-1':'#e60000'
          }

        self.line_color = {'3':'ffe600e6',
              '2':'ff003ae6',
              '1':'ff00e674',
              '0':'fface600',
              '-1':'ffe60000'
              }

        self.csv = open(csv,'r')
        self.csv_filename = os.path.basename(csv)
        self.drive_name = os.path.splitext(self.csv_filename)[0]

        

    def kml(self):

        self.kml_name = self.drive_name+'.kml'
        count = 0
        with open(self.kml_name, 'w') as kml:
            kml.write(self.header)
            kml.write(self.ledgend)
            name = self.name.format(self.drive_name)
            kml.write(name)
            for row in self.csv:
                cell = row.split(',')
                if count == 0:
                    count += 1
                    continue

                if count == 1:
                    lat2 = cell[0]
                    lon2 = cell[1]
                else:
                    lat2 = lat1
                    lon2 = lon1
                
                lat1 = cell[0]
                lon1 = cell[1]
                
                up = float(cell[2])
                
                if 3 <= up:
                    up = self.color['3']
                    lc = self.line_color['3']
                elif 2 <= up < 3:
                    up = self.color['2']
                    lc = self.line_color['2']
                elif 1 <= up < 2:
                    up = self.color['1']
                    lc = self.line_color['1']
                elif 0 <= up < 1:
                    up = self.color['0']
                    lc = self.line_color['0']
                elif up < 0:
                    up = self.color['-1']
                    lc = self.line_color['-1']


                track = self.placemark.format(c=up,
                                              r=count,
                                              lon1=lon1,
                                              lat1=lat1,
                                              lon2=lon2,
                                              lat2=lat2,
                                              lc=lc)
                                         
                kml.write(track)
                count += 1

            kml.write(self.footer)
            kml.close
            self.csv.close







if __name__ == '__main__':
    generate = generate('20180620-Long.csv')
    generate.kml()

    
