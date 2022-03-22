from operator import itemgetter

class ShopManager:
    def __init__(self, _osm):
        self.osm = _osm
    
    def getCountsOfTypes(self):
        countDict = []
        
        def isInDict(type):
            for a in countDict:
                if a['type'] == type:
                    return True
            return False

        if self.osm.shopList:
            for shop in self.osm.shopList:
                if not isInDict(shop.type):
                    countDict.append({'type': shop.type, 'count': sum(a.type == shop.type for a in self.osm.shopList)})
                
            return sorted(countDict, key=itemgetter('count'), reverse=True) 
