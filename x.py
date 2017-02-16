
import pandas as pd
from urllib2 import Request, urlopen
import json

import sys
print sys.argv[1]

#address = 'Seven%20Sea%20Condo'
address = sys.argv[1]
request=Request('http://maps.google.com/maps/api/geocode/json?address='+address)
response = urlopen(request)
elevations = response.read()
#print(elevations.splitlines())
pd.read_json(elevations)

data = json.loads(elevations)
lat,lng,el = [],[],[]


lat = 0 
lng = 0
for result in data['results']:
    #lat.append(result['location']['lat'])
    #lng.append(result[u'location'][u'lng'])
    #print(result)
    print(result[u'geometry'][u'location'][u'lat'])
    print(result[u'geometry'][u'location'][u'lng'])
    lat = result[u'geometry'][u'location'][u'lat']
    lng = result[u'geometry'][u'location'][u'lng']
    break


#df = pd.DataFrame([lat,lng,el]).T
#print(df)
#file = open('output.csv', 'w')
file = open('output.csv','a')
file.write(address+","+str(lat)+","+str(lng)+"\n")
file.close()
