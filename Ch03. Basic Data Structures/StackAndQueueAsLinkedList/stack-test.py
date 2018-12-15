from Stack import Stack

def reverseString(string):
	s = Stack()
	for character in string:
		s.push(character)

	result = ""
	while not s.isEmpty():
		result += s.pop()

	return result

print(reverseString("This is my string!"))