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

class Converter:
	def __init__(self, exp):
		self.exp = exp
		self.operatorStack = Stack()

	def setExpression(self, exp):
		self.exp = exp

	def isOperand(self, x):
		if not x in ['+', '-', '/', '*', '^', '(', ')']:
			return True
		return False

	def hasMorePrecedence(self, val , top):
		if top==-1:
			return True
		elif val=='^':
			return True
		elif top=='^' and not val=='^':
			return False
		elif (top=='*' or top=='/') and (val=='*' or val=='/' and val=='^'):
			return True
		elif (top=='+' or top=='-') and (val=='+' or val=='-' or val=='*' or val=='/'):
			return True
		else:
			return False

	def pushToStackOrToOutput(self, x):
		output = ''
		if self.hasMorePrecedence(x , self.operatorStack.top()):
			self.operatorStack.push(x)
		else:
			while not self.hasMorePrecedence(x , self.operatorStack.top()):
				if self.operatorStack.isEmpty():
					break
				val = self.operatorStack.pop()
				if val=='(':
					self.operatorStack.push(val)
					break
				output += val
			self.operatorStack.push(x)
		return output


	def getValuesFromStack(self):
		output = ''
		while True:
			x = self.operatorStack.pop()
			if x=='(' or x==-1:
				break
			output += x
		return output


	def convert(self):
		output = ''
		for x in exp:
			if self.isOperand(x):
				output += x
			elif x=='(':
				self.operatorStack.push(x)
			elif x==')':
				out = self.getValuesFromStack()
				output += out
			else:
				out = self.pushToStackOrToOutput(x)
				output += out
		while not self.operatorStack.isEmpty():
			output += self.operatorStack.pop()
		return output



if __name__ == '__main__':
	exp = "a+b*(c^d-e)^(f+g*h)-i"
	con = Converter(exp)
	print(con.convert())
	exp = 'A+B*C+D'
	con.setExpression(exp)
	print(con.convert())


