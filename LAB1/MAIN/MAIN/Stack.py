class Stack:
	def __init__(self):
		self.item = []
	def size(self):
		return len(self.item)
	def push(self, sth):
		self.item.append(sth)
	def isEmpty(self):
		return self.size() == 0
	def pop(self, index=None):
		if index is None:
			self.item.pop()
		else:
			self.item.pop(index)
	def peek(self):
		return self.item[-1]
	def __str__(self):
		return str(self.item)
