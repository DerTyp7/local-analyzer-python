
# ! "amenity" are used very often in osm it's referreing to healtcare, police, cafe, pub, ice cream, post etc.
# ! There is defently a need to sort them more on not just take them all into a "amenity" class

# TODO new objects: healthcare, police

# ? offices 
# ? How to handle districts

class Shop:
    # TODO More optional details/attributes. Example: "website", "brand", "Telefone", "Owner", "opening times"
    def __init__(self, _nodeIds, _name, _type):
        self.nodeIds = _nodeIds
        self.name = _name
        self.type = _type

class Node:
    def __init__(self, _id, _lon, _lat, _version, _timestamp, _changeset, _uid, _user):
        self.id = int(_id)
        self.lon = str(_lon)
        self.lat = str(_lat)
        self.version = str(_version)
        self.timestamp = str(_timestamp)
        self.changeset = int(_changeset)
        self.uid = int(_uid)
        self.user = str(_user)


class NodeTag:
    def __init__(self, _id, _nodeId, _key, _value):
        self.id = int(_id)
        self.nodeId = int(_nodeId)
        self.key = str(_key)
        self.value = str(_value)

class Way:
    def __init__(self, _id, _version, _timestamp, _changeset, _uid, _user):
        self.id = int(_id)
        self.version = str(_version)
        self.timestamp = str(_timestamp)
        self.changeset = int(_changeset)
        self.uid = int(_uid)
        self.user = str(_user)


class WayTag:
    def __init__(self, _id, _wayId, _key, _value):
        self.id = int(_id)
        self.wayId = int(_wayId)
        self.key = str(_key)
        self.value = str(_value)
