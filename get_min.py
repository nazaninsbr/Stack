class Stack:
	def __init__(self):
		self.values = []
		self.min = ''

	def push(self, x):
		self.values.append(x)
		if self.min=='':
			self.min=x
		elif self.min > x:
			self.min = x

	def top(self):
		if len(self.values)==0:
			return -1
		return self.values[-1]

	def isEmpty(self):
		if len(self.values)==0:
			return True
		return False

	def pop(self):
		if not self.isEmpty():
			x = self.values[-1]
			del self.values[-1]
			return x
		return -1

	def insertAtBottom(self, item):
		if self.isEmpty():
			self.push(item)
		else:
			temp = self.pop()
			self.insertAtBottom(item)
			self.push(temp)

	def seeLastElement(self):
		tempStack = Stack()
		while not self.isEmpty():
			x = self.pop()
			tempStack.push(x)

		returnVal = tempStack.top()

		while not tempStack.isEmpty():
			x = tempStack.pop()
			self.push(x)
		return returnVal

	def getMin(self):
		return self.min


if __name__ == '__main__':
	s = Stack()
	s.push(12)
	s.push(1)
	s.push(8)
	s.push(122)
	s.push(-12)
	print(s.getMin())