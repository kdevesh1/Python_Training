# Write the program to get the name of user and reverse it 

word = input("Input a word to reverse: ")

for ch in range(len(word) - 1, -1, -1):
  print(word[ch],end="")

