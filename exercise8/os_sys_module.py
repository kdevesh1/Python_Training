# 

 
import sys
import os
 
print(sys.version)

print(os.name) 
#print("Hello {}. Welcome to {} tutorial".format(sys.argv[0],sys.argv[1], sys.argv[2]))

print(sys.path)   #  This is an environment variable that is a search path for all Python modules. 
#print(os.ls-R)
print(sys.maxsize)

print(os.getcwd())     # it returns current working directory

try: 
    # If the file does not exist, 
    # then it would throw an IOError 
    filename = 'GFG.txt'
    f = open(filename, 'rU') 
    text = f.read() 
    f.close() 
  
# Control jumps directly to here if  
#any of the above lines throws IOError.     
except IOError: 
  
    # print(os.error) will <class 'OSError'> 
    print('Problem reading:', filename) 
      
# In any case, the code then continues with  
# the line after the try/except 



