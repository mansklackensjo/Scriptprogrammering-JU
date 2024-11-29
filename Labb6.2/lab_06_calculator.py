class Calculator:
	def __init__(self, initial_memory_value):
		self.memory_value: float = initial_memory_value
		self.history:list[float] = []

	def get_memory_value(self):
		return self.memory_value
	
	def get_history(self):
		return self.history

	def add(self, operand: float):
		self.memory_value += operand
		self.history.append(self.memory_value)

	def subtract(self, operand: float):
		self.memory_value -= operand
		self.history.append(self.memory_value)

	def multiply(self, operand: float):
		self.memory_value *= operand
		self.history.append(self.memory_value)

	def divide(self, operand: float):
		self.memory_value /= operand
		self.history.append(self.memory_value)

	def can_undo(self):
		if len(self.history) > 1:
			return True
		else:
			return False
		
	def undo(self):
		self.history.pop()
		self.memory_value = self.history[-1]

	
