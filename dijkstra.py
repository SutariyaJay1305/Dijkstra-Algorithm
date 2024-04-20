class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def displayResults(self, dist):
		print("Vertex \t Distance from Source")
		for node in range(self.V):
			print(node, "\t\t", dist[node])


	def findMinDistance(self, dist, sptSet):

		minimum = float('inf')

		for v in range(self.V):
			if dist[v] < minimum and sptSet[v] == False:
				minimum = dist[v]
				min_index = v

		return min_index

	def computeShortestPath(self, src):

		dist = [float('inf')] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for _ in range(self.V):
			u = self.findMinDistance(dist, sptSet)

			
			sptSet[u] = True

			
			for v in range(self.V):
				if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]

		self.displayResults(dist)

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, 0, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, 0, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, 0, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, 0, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, 0, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, 0, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, 0, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, 0]
		]

g.computeShortestPath(0)
