# Write the program to break the loop if user give n as input, if y continue

str = str(input("enter any string : "))

for val in str:
    if val == 'n':
        break
    elif val == 'y':
        continue
    else:
        print(val)
print(" the end")

    
