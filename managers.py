from operator import itemgetter

class PlaceManager:
    def __init__(self, _osm):
        self.osm = _osm
    
    def getCountsOfTypes(self):
        countDict = []
        
        def isInDict(type):
            for a in countDict:
                if a['type'] == type:
                    return True
            return False

        if self.osm.placeList:
            for place in self.osm.placeList:
                if not isInDict(place.type):
                    countDict.append({'type': place.type, 'count': sum(a.type == place.type for a in self.osm.placeList)})
                
            return sorted(countDict, key=itemgetter('count'), reverse=True) 
    
    def getPlacesByType(self, type):
        result = []
        for a in self.osm.placeList:
            if a.type == type:
                result.append(a)

        return result

    def getPlacesByName(self, name):
        result = []
        for a in self.osm.placeList:
            if a.name == name:
                result.append(a)

        return result