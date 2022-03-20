# https://overpass-api.de/api/map?bbox=8.59993,53.52150,8.61004,53.52484
# links - unten - rechts - oben
# minLon - minLat - maxLon - maxLat
import requests
from init_sql import parseOsmToSql

lon = 8.6039883
lat = 52.51608

# TODO Get real value based on a metric radius
areaHeightRadius = 0.01 # 0.01
areaWidthRadius = 0.013 # 0.013

minLon = round(float(lon) - areaWidthRadius, 5)
maxLon = round(float(lon) + areaWidthRadius, 5)

minLat = round(float(lat) - areaHeightRadius, 5)
maxLat = round(float(lat) + areaHeightRadius, 5)

requestUrl = "https://overpass-api.de/api/map" 
requestsUrlParams = f"?bbox={minLon},{minLat},{maxLon},{maxLat}"



print(requestUrl + requestsUrlParams)

headers = {'Content-Type': 'application/xml'}
r = requests.get(requestUrl + requestsUrlParams, headers=headers)

osmContent = r.text
parseOsmToSql(osmContent, "database.db")