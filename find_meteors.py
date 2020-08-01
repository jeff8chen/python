
import math
import requests

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

def get_dist(meteor):
    return meteor.get('distance', math.inf)

my_loc = (40.2892, -75.2149)

meteor_resp = requests.get('https://data.nasa.gov/resource/y77d-th95.json')
meteor_data = meteor_resp.json()
# meteor_data is a list of dictionary as follows:
#{"name":"Aachen","id":"1","nametype":"Valid","recclass":"L5","mass":"21","fall":"Fell","year":"1880-01-01T00:00:00.000",
#"reclat":"50.775000","reclong":"6.083330","geolocation":{"type":"Point","coordinates":[6.08333,50.775]}}

#if no lat or long, then skip.
#otherwise, calculate the distance, then add it to the dictionary meteor_data.
for meteor in meteor_data:
    if not ('reclat' in meteor and 'reclong' in meteor): continue
    meteor['distance'] = calc_dist(float(meteor['reclat']),
                                   float(meteor['reclong']),
                                   my_loc[0],
                                   my_loc[1])
meteor_data.sort(key=get_dist)

#print top 10 closest meteors.
for m in meteor_data[0:10]:
    print(m)
    print("\n")
