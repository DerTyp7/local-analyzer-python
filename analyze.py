OFFLINE = False
from managers import PlaceManager
from osm import OSM
from publicTransport import PublicTransportAccessibility
import requests

# ADVANCED:
# Get external data of shops, like website
# Get General City/Region data: average age, peace index, democrazy index, average income  

# IDEAS:
# Parks
# ATMs

# 52.9152386,,15.96z
# bhv 53.51500036203292, 8.603602165157444
"""
# TODO Get User input
lon = 8.8285578 # 8.6039883
lat = 52.9152386  # 52.51608

"""

def get_data(lon, lat):
        
    # TODO Get real value based on a metric radius
    areaHeightRadius = 0.01 # 0.01
    areaWidthRadius = 0.013 # 0.013

    minLon = round(float(lon) - areaWidthRadius, 5)
    maxLon = round(float(lon) + areaWidthRadius, 5)

    minLat = round(float(lat) - areaHeightRadius, 5)
    maxLat = round(float(lat) + areaHeightRadius, 5)

    requestUrl = "https://overpass-api.de/api/map" 
    requestsUrlParams = f"?bbox={minLon},{minLat},{maxLon},{maxLat}"


    if OFFLINE:
        print("Using offline file!")
        file = open("mapHH", encoding="utf8")
        osm = OSM(file.read())
    else:
        print(requestUrl + requestsUrlParams)
        print("Downloading OSM-File...")
        # TODO Check if banned from overpass-api MAYBE get alternative API then
        r = requests.get(requestUrl + requestsUrlParams, headers={'Content-Type': 'application/xml'})
        print("Done: Downloading OSM-File")
        osm = OSM(r.text)

    pta = PublicTransportAccessibility(osm)
    placeManager = PlaceManager(osm)
    
    print("\n--- Public Transport Accessibility ---")
    print("Bus:        " + str(pta.isBusAccessible()))
    print("Tram:       " + str(pta.isTramAccessible()))
    print("Light Rail: " + str(pta.isLightRailAccessible()))
    print("Subway:     " + str(pta.isSubwayAccessible()))
    print("Train:      " + str(pta.isTrainAccessible()))
    print("Monorail:   " + str(pta.isMonorailAccessible()))

    print("\n--- 20 Most present places types ---")
    counter = 0
    for s in placeManager.getCountsOfTypes():
        if counter <= 20:
            print(s['type'] + " : " + str(s['count']) + " times")
        counter = counter + 1