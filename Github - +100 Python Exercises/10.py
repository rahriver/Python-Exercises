words = input('Words: ').split(' ')

for word in words:
    if words.count(word) > 1:
        words.remove(word)

alpha = sorted(words, key=lambda x: len(x))
print(' '.join(alpha))

