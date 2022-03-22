from operator import itemgetter

class Shops:
    def __init__(self, _osm):
        self.osm = _osm
    
    def getAllShopTypes(self):
        shopList = []
        
        for tag in self.osm.nodeTagList:
            if tag.key == "shop":
                shopList.append(tag.value)

        for tag in self.osm.wayTagList:
            if tag.key == "shop":
                shopList.append(tag.value)
        return shopList

    def countOfShopTypes(self):
        shopList = self.getAllShopTypes()
        countDict = []
        
        if shopList:
            def isInDict(name):
                for a in countDict:
                    if a['type'] == name:
                        return True
                return False

            for shop in shopList:
                print(shop)
                if not isInDict(shop):
                    print("add" + str(shopList.count(shop)))
                    countDict.append({'type': shop, 'count': shopList.count(shop)})
            return sorted(countDict, key=itemgetter('count'), reverse=True) 