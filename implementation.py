class Stack:
	def __init__(self):
		self.values = []

	def push(self, x):
		self.values.append(x)

	def top(self):
		if len(self.values)==0:
			return -1
		return self.values[-1]

	def pop(self):
		if len(self.values)==0:
			return -1
		x = self.values[-1]
		del self.values[-1]
		return x


if __name__ == '__main__':
	s = Stack()
	s.push(12)
	s.push(1)
	s.push(8)
	s.push(122)
	s.push(-12)
	print(s.top())
	s.pop()
	s.pop()
	print(s.top())