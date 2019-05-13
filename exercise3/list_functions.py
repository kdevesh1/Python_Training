# Use list functions append(), count(), extend(), index(), insert(), pop(), remove(), reverse() and sort()  

my_list = [3, 8, 1, 6, 0, 8, 4]

print(my_list.index(8))

print(my_list.count(8))

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

my_list.append(7)
print(my_list)	

my_list.pop()
print(my_list)	

my_list.extend([1,3,5])
print(my_list)

my_list.remove(3)
print(my_list)

my_list.insert(7,1)
print(my_list)
