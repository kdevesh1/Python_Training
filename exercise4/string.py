# Given a string, return a string where for every char in the original, there are two chars. Eg. double_char(The) = TThhee


string = raw_input("Enter the string : ")

def fun1(string):
	double = 2
	result = ''.join([char * double for char in string])
	return result

result = fun1(string)
print(result)
