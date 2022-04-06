sent = list(input("Say Something: "))
sentence = "".join([char for char in sent if char not in "aeiou"])
print(sentence)
