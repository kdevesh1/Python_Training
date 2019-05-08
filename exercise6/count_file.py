 #Write a program to count how many lines in a txt files 

fname=input("Enter the file path : ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)


