# Write a Python program to read last n lines of a file.


def lastnlines(f,n):
    with open(f) as file:
        print('Last',n,'lines from file :',f)
        for line in (file.readlines()[-n:]):
            print(line,end=' ')

name=input("enter the file name:")
n=int(input('No of last lines to read :'))
try:
    lastnlines(name,n)
except:
    print('Lines error ......')

