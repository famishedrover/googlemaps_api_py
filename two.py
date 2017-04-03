import requests
from pprint import pprint
from sys import argv

def gcode(address) :
	url = 'https://maps.googleapis.com/maps/api/geocode/json'
	r = requests.get(url , params = {'address' : address})
	return r.json()
try :
	location =  argv[1]
except :
	print 'using default location search to "Delhi Technological University"'
	location = 'Delhi Technological University'

data = gcode(location)

print 'Address   : %s'%(data['results'][0]['formatted_address'])
g = (data['results'][0]['geometry']['location'])
lat = g['lat']
lng = g['lng']
print 'Latitude  : %s\nLongitude : %s'%(str(lat) , str(lng) )
# print g
# print lat , lng
# pprint(data)
