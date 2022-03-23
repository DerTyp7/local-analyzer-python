from objects.baseObjects import Node, NodeTag, Way, WayTag, Place
from objects.metaObjects import Address, Contact

class OSM:
	# TODO Average value of "last updated" to see how up to date the data is.
	def __init__(self, _osmContent):
		self.osmContent = str(_osmContent)
		self.nodeList = []
		self.nodeTagList = []
		self.wayList = []
		self.wayTagList = []
		self.placeList = []

		self.parseOsmContent()

	def parseOsmContent(self):
		lines = self.osmContent.split("\n")

		nodeLines = []
		wayLines = []

		for line in lines:
			if "<node" in line:
				if "/>" in line:
					try:
						self.createNode([line])
					except:
						print("Node could not be inserted")
				else:
					nodeLines.append(line)
			elif "</node>" in line:
				try:
					self.createNode(nodeLines)
				except:
					print("Node could not be inserted")
				nodeLines = []
			elif len(nodeLines) > 0:
				nodeLines.append(line)
			elif "<way" in line:
				wayLines.append(line)
			elif "</way>" in line:
				try:
					self.createWay(wayLines)
				except:
					print("Way could not be inserted")
				wayLines = []
			elif len(wayLines) > 0:
				wayLines.append(line)

	def createContact(self, lines):
		c = Contact()

		for line in lines:
			if '<tag ' in line:
				key = str(line.split('k="')[1].split('"')[0])
				value = str(line.split('v="')[1].split('"')[0]) 

				if key == "contact:website" or key == "website":
					c.website = value
				elif key == "contact:phone" or key == "phone":
					c.phone = value
				elif key == "contact:mobile" or key == "mobile":
					c.mobile = value
				elif key == "contact:fax" or key == "fax":
					c.fax = value
				elif key == "contact:email" or key == "email":
					c.email = value
				elif key == "contact:facebook":
					c.facebook = value
				elif key == "contact:vk":
					c.vk = value
				elif key == "contact:instagram":
					c.instagram = value
				elif key == "contact:twitter":
					c.twitter = value
				elif key == "contact:youtube":
					c.youtube = value
				elif key == "contact:ok":
					c.ok = value
				elif key == "contact:webcam":
					c.webcam = value
				elif key == "contact:telegram":
					c.telegram = value
				elif key == "contact:whatsapp":
					c.whatsapp = value
				elif key == "contact:linkedin":
					c.linkedin = value
				elif key == "contact:pinterest":
					c.pinterest = value
				elif key == "contact:viper":
					c.viper = value
				elif key == "contact:foursquare":
					c.foursquare = value
				elif key == "contact:skype":
					c.skype = value
				elif key == "contact:xing":
					c.xing = value
				elif key == "contact:vhf":
					c.vhf = value
				elif key == "contact:flickr":
					c.flickr = value
				elif key == "contact:mastodon":
					c.mastodon = value
				elif key == "contact:sip":
					c.sip = value
				elif key == "contact:diaspora":
					c.diaspora = value
				elif key == "contact:gnusocial":
					c.gnusocial = value
		return c

	def createAddress(self, lines):
		a = Address()

		for line in lines:
			if '<tag ' in line:
				key = str(line.split('k="')[1].split('"')[0])
				value = str(line.split('v="')[1].split('"')[0]) 

				if key == "addr:housenumber":
					a.housenumber = value
				elif key == "addr:street":
					a.street = value
				elif key == "addr:place":
					a.place = value
				elif key == "addr:city":
					a.city = value
				elif key == "addr:postcode":
					a.postcode = value
				elif key == "addr:country":
					a.country = value
				elif key == "addr:suburb":
					a.suburb = value
				elif key == "addr:state":
					a.state = value
				elif key == "addr:province":
					a.province = value
		return a

	def createPlace(self, lines, isShop):
		# TODO Make sure shops are not duplicates.
		# TODO e.g. REWE(shop) is big enough to have some "Ways" of it's own and multiple nodes, which can cause duplicates.

		nodeIds = []
		type = ""
		name = ""
		openingHours = ""

		address = self.createAddress(lines)
		contact = self.createContact(lines)

		for line in lines:
			if '<tag ' in line:
				key = str(line.split('k="')[1].split('"')[0])
				value = str(line.split('v="')[1].split('"')[0]) 

				if key == "amenity" and not isShop:
					type = value
				elif key == "shop" and isShop:
					type = value
				elif key == "name":
					name = value
				elif key == "opening_hours":
					openingHours = value

			elif '<nd ' in line:
				nodeIds.append(line.split('ref="')[1].split('"')[0])
			elif "<node" in line:
				nodeIds.append(str(line.split('id="')[1].split('"')[0]))

		p = Place(nodeIds, type, name, address, contact, openingHours)
		self.placeList.append(p)

	def createWay(self, lines):
		wayId = ""

		for line in lines:
			if "<way" in line:
				wayId = str(line.split('id="')[1].split('"')[0])
				wayVersion = str(line.split('version="')[1].split('"')[0])
				wayTimestamp = str(line.split('timestamp="')[1].split('"')[0])
				wayChangeset = str(line.split('changeset="')[1].split('"')[0])
				wayUid = str(line.split('uid="')[1].split('"')[0])
				wayUser = str(line.split('user="')[1].split('"')[0])

				w = Way(wayId, wayVersion, wayTimestamp, wayChangeset, wayUid, wayUser)
				self.wayList.append(w)

			elif '<tag ' in line:
				key = str(line.split('k="')[1].split('"')[0])
				value = str(line.split('v="')[1].split('"')[0]) 
				wt = WayTag(len(self.wayTagList), wayId, key, value)
				self.wayTagList.append(wt)

				if key == "shop":
					self.createPlace(lines, True)
				elif key == "amenity":
					self.createPlace(lines, False)

	def createNode(self, lines):
		nodeId = ""

		for line in lines:
			if "<node" in line:
				nodeId = str(line.split('id="')[1].split('"')[0])
				nodeLon = str(line.split('lon="')[1].split('"')[0])
				nodeLat = str(line.split('lat="')[1].split('"')[0])
				nodeVersion = str(line.split('version="')[1].split('"')[0])
				nodeTimestamp = str(line.split('timestamp="')[1].split('"')[0])
				nodeChangeset = str(line.split('changeset="')[1].split('"')[0])
				nodeUid = str(line.split('uid="')[1].split('"')[0])
				nodeUser = str(line.split('user="')[1].split('"')[0])

				n = Node(nodeId, nodeLon, nodeLat, nodeVersion, nodeTimestamp, nodeChangeset, nodeUid, nodeUser)
				self.nodeList.append(n)

			elif '<tag ' in line:
				key = str(line.split('k="')[1].split('"')[0])
				value = str(line.split('v="')[1].split('"')[0]) 
				nt = NodeTag(len(self.nodeTagList), nodeId, key, value)
				self.nodeTagList.append(nt)

				if key == "shop":
					self.createPlace(lines, True)
				elif key == "amenity":
					self.createPlace(lines, False)