# Intilializes/Creates the database with all tables and table contents
import sqlite3

def createNode(conn, lines):
	nodeId = ""
	cur = conn.cursor()


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

			cur.execute('INSERT INTO nodes("id", "lon", "lat", "version", "timestamp", "changeset", "uid", "user") VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
			(nodeId, nodeLon, nodeLat, nodeVersion, nodeTimestamp, nodeChangeset, nodeUid, nodeUser))

		elif '<tag ' in line:
			print("HALLO")
			key = str(line.split('k="')[1].split('"')[0])
			value = str(line.split('v="')[1].split('"')[0]) 
			cur.execute('INSERT INTO node_tags("nodeId", "key", "value") VALUES (?,?,?)', (nodeId, key, value))


def createWay(conn, lines):
	wayId = ""
	wayNodes = []
	cur = conn.cursor()

	for line in lines:
		if "<way" in line:
			wayId = str(line.split('id="')[1].split('"')[0])
			wayVersion = str(line.split('version="')[1].split('"')[0])
			wayTimestamp = str(line.split('timestamp="')[1].split('"')[0])
			wayChangeset = str(line.split('changeset="')[1].split('"')[0])
			wayUid = str(line.split('uid="')[1].split('"')[0])
			wayUser = str(line.split('user="')[1].split('"')[0])

			cur.execute('INSERT INTO ways("id", "version", "timestamp", "changeset", "uid", "user") VALUES (?,?,?,?,?,?)',
	 			(wayId, wayVersion, wayTimestamp, wayChangeset, wayUid, wayUser))

		elif "<nd ref=" in line:
			wayNodes.append(str(line.split('ref="')[1].split('"')[0]))
		elif '<tag ' in line:
			key = str(line.split('k="')[1].split('"')[0])
			value = str(line.split('v="')[1].split('"')[0]) 
			cur.execute('INSERT INTO way_tags("wayId", "key", "value") VALUES (?,?,?)', (wayId, key, value))
	
	

	for nodeId in wayNodes:
		createNodeWayJunction(conn, wayId, nodeId)

def createNodeWayJunction(conn, wayId, nodeId):
	cur = conn.cursor()
	cur.execute('INSERT INTO node_way(wayId, nodeId) VALUES (?, ?)', (wayId, nodeId))

def createDatabase(path):
	try:
		print("Generate database structure")
		conn = sqlite3.connect(path)
		cur = conn.cursor()

		cur.execute('''CREATE TABLE "nodes" (
						"id"	INTEGER NOT NULL UNIQUE,
						"lon"	TEXT NOT NULL,
						"lat"	TEXT NOT NULL,
						"version"	INTEGER NOT NULL,
						"timestamp"	TEXT NOT NULL,
						"changeset"	TEXT NOT NULL,
						"uid"	INTEGER NOT NULL,
						"user"	TEXT NOT NULL,
						PRIMARY KEY("id")
					);''')

		cur.execute('''CREATE TABLE "ways" (
						"id"	INTEGER NOT NULL UNIQUE,
						"version"	INTEGER NOT NULL,
						"timestamp"	TEXT NOT NULL,
						"changeset"	TEXT NOT NULL,
						"uid"	INTEGER NOT NULL,
						"user"	TEXT NOT NULL,
						PRIMARY KEY("id")
					);''')
		
		cur.execute('''CREATE TABLE "way_tags" (
						"id"	INTEGER NOT NULL UNIQUE,
						"wayId"	INTEGER NOT NULL,
						"key"	TEXT,
						"value"	TEXT,
						PRIMARY KEY("id" AUTOINCREMENT),
						FOREIGN KEY("wayId") REFERENCES "ways"("id")
					);''')
		
		cur.execute('''CREATE TABLE "node_tags" (
						"id"	INTEGER NOT NULL UNIQUE,
						"nodeId"	INTEGER NOT NULL,
						"key"	TEXT,
						"value"	TEXT,
						PRIMARY KEY("id" AUTOINCREMENT),
						FOREIGN KEY("nodeId") REFERENCES "nodes"("id")
					);''')

		cur.execute('''CREATE TABLE "node_way" (
						"id"	INTEGER NOT NULL UNIQUE,
						"wayId"	INTEGER NOT NULL,
						"nodeId"	INTEGER NOT NULL,
						PRIMARY KEY("id"),
						FOREIGN KEY("wayId") REFERENCES "ways"("id"),
						FOREIGN KEY("nodeId") REFERENCES "nodes"("id")
					);''')	

		return conn
	except:
		return sqlite3.connect(path)

# INIT
def parseOsmToSql(osmContent, path):
	print("Initializing database. This may take a while.")
	conn = createDatabase(path)

	print("Parsing nodes and ways of the OSM file into the database.")
	wayLines = []
	nodeLines = []
	lines = osmContent.split("\n")

	for line in lines:
		if "<node" in line:
			if "/>" in line:
				try:
					createNode(conn, [line])
				except:
					print("Node could not be inserted")
			else:
				nodeLines.append(line)
		elif "</node>" in line:
			print("CREATE")
			try:
				createNode(conn, nodeLines)
			except:
				print("Node could not be inserted")
			nodeLines = []
		elif len(nodeLines) > 0:
			print("Append")
			nodeLines.append(line)
			
		elif "<way " in line:
			wayLines.append(line)
		elif "</way>" in line:
			try:
				createWay(conn, wayLines)
			except:
				print("Way could not be inserted")
			wayLines = []
		elif len(wayLines) > 0:
			wayLines.append(line)

	conn.commit()
	conn.close()
	print("Done: Initializing database")