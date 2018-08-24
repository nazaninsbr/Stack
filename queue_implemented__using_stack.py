class Stack:
	def __init__(self):
		self.values = []

	def push(self, x):
		self.values.append(x)

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

class Queue:
	def __init__(self):
		self.stack = Stack()

	def enqueue(self, val):
		self.stack.insertAtBottom(val)

	def dequeue(self):
		return self.stack.pop()

	def front(self):
		return self.stack.top()

	def rear(self):
		return self.stack.seeLastElement()


if __name__ == '__main__':
	q = Queue()
	q.enqueue(12)
	q.enqueue(1233)
	q.enqueue(-12)
	q.enqueue(66)
	print('Front: ', q.front())
	print('Rear: ', q.rear())
	print(q.stack.values)
	q.dequeue()
	q.dequeue()
	print(q.stack.values)

