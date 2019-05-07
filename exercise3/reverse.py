#  

word = input("Input a word to reverse: ")

for ch in range(len(word) - 1, -1, -1):
  print(word[ch],end="")
print("\n")
