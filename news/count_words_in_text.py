import re

from collections import Counter

# make list of all words from text
words = re.findall('\w+', open('text.json').read().lower())
print(words)


distance = int(input('Please input distance = '))
lst = []
for word in words:
    if 'is' == word:
        index = words.index(word)
        for i in range(distance):
            lst.append(words[index - i - 1])
        lst.append(word.upper())
        for i in range(distance):
            lst.append(words[index + i + 1])
        words.pop(index)

print(lst)
print(Counter(lst).most_common())
#print(Counter(words).most_common(10))



