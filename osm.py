from objects import 
class OSM:
	def __init__(self, _osmContent):
		self.osmContent = str(_osmContent)
		self.nodeList = []
		self.parseOsmContent()

	def parseOsmContent(self):
		lines = self.osmContent.split("\n")
		
		wayLines = []
		nodeLines = []

		for line in lines:
			if "<node" in line:
				if "/>" in line:
					try:
						self.createNode(conn, [line])
					except:
						print("Node could not be inserted")
				else:
					nodeLines.append(line)
			elif "</node>" in line:
				try:
					self.createNode(conn, nodeLines)
				except:
					print("Node could not be inserted")
				nodeLines = []
			elif len(nodeLines) > 0:
				nodeLines.append(line)
				
			elif "<way " in line:
				wayLines.append(line)
			elif "</way>" in line:
				try:
					#self.createWay(conn, wayLines)
				except:
					print("Way could not be inserted")
				wayLines = []
			elif len(wayLines) > 0:
				wayLines.append(line)

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

				n = Node
				cur.execute('INSERT INTO nodes("id", "lon", "lat", "version", "timestamp", "changeset", "uid", "user") VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
				(nodeId, nodeLon, nodeLat, nodeVersion, nodeTimestamp, nodeChangeset, nodeUid, nodeUser))

			elif '<tag ' in line:
				print("HALLO")
				key = str(line.split('k="')[1].split('"')[0])
				value = str(line.split('v="')[1].split('"')[0]) 
				cur.execute('INSERT INTO node_tags("nodeId", "key", "value") VALUES (?,?,?)', (nodeId, key, value))