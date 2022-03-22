from objects import Node, NodeTag, Way, WayTag

class OSM:
	def __init__(self, _osmContent):
		self.osmContent = str(_osmContent)
		self.nodeList = []
		self.nodeTagList = []
		self.wayList = []
		self.wayTagList = []
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