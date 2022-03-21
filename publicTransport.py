from osm import OSM
from objects import Node, NodeTag

class PublicTransportAccessibility:
    def __init__(self, _osm):
        self.osm = _osm
    
    def isBusAccessible(self):
        for tag in self.osm.nodeTagList:
            if tag.key == "highway" and tag.value == "bus_stop":
                return True
        return False
    
    def isTramAccessible(self):
        for tag in self.osm.nodeTagList:
            if tag.key == "railway" and tag.value == "tram_stop":
                return True
        return False
    
    def isTrainAccessible(self):
        for tag in self.osm.nodeTagList:
            if tag.key == "railway" and tag.value == "station":
                return True
        return False
    
    def isLightRailAccessible(self):
        for tag in self.osm.nodeTagList:
            if tag.key == "station" and tag.value == "light_rail":
                return True
        return False
    
    def isSubwayAccessible(self):
        for tag in self.osm.nodeTagList:
            if tag.key == "station" and tag.value == "subway":
                return True
        return False

    def isMonorailAccessible(self):
        for tag in self.osm.nodeTagList:
            if tag.key == "station" and tag.value == "monorail":
                return True
        return False