class State():
	def __init__(self,parent,hvalue,child,label):
		self.parent=parent
		self.hvalue=hvalue
		self.child=child
		self.label=label
	def __eq__(self, other):
		if other == None or self == None:
			return False
		return self.label == other.label
class Graph():
	def __init__(self, giveinput):
		self.n = giveinput['nodes']
		self.w = giveinput['weight']
		self.al = giveinput['adj_l']
		self.ss = giveinput['ss']
		self.gs = giveinput['gs']
		if giveinput['weight'] == False:
			for i in self.al:
				for j in self.al[i]:
					t = self.al[i].pop(0)
					self.al[i].append((t, 0))
		self.hvalue_table = {}
					
	def cost(self, current, next):
		for i in self.al[current]:
			if i[0] == next:
				return i[1]
		return -1
		
	def neighbors(self, current):
		return [i[0] for i in self.al[current]]
class PriorityQueue():
	def __init__(self):
		self.q = []
		self.len = 0

	def put(self, val):
		if self.len == 0:
			self.q.append(val)
		else:
			i = 0
			while i < self.len and self.q[i].hvalue < val.hvalue:
				i += 1
			self.q.insert(i, val)
		self.len += 1
		
	def pop(self):
		self.len -= 1
		return self.q.pop(0)
		
	def top_node(self):
		return self.q[0]

	def extend(self, pq):
		for i in pq.q:
			self.put(i)	
	
	
