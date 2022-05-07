class DisjointSet:
	def __init__(self, maxn):
		self.maxn = maxn
		self.size = [1] * maxn
		self.parent = [i for i in range(maxn)]

	def find(self, v):
		if (v == self.parent[v]):
			return v

			self.parent[v] = self.find(self.parent[v])
			return self.parent[v]

	def union(self, a, b):
		a = self.find(a)
		b = self.find(b)
		if a != b:
			if self.size[a] < self.size[b]:
				a, b = b, a

			self.parent[b] = a
			self.size[a] += self.size[b]