#Write a program to strictly accept interger as input.  

while True:
    try:
        num=int(input("enter any number :"))
    except ValueError:
        print("please enter only integer number: ")
    except:
        print("unsucessful")         
    else :
        print(num)
        break


