


string = raw_input("Enter the string : ")

def fun1(string):
	double = 2
	result = ''.join([char * double for char in string])
	return result

result = fun1(string)
print(result)
