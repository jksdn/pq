sentence = "This is a common interview question"

char_frequency = {}

from pprint import pprint

for char in sentence:
  if char in char_frequency:
    char_frequency[char] = char_frequency[char] + 1
  else:
    char_frequency[char] = 1

char_frequency_sorted = sorted(char_frequency.items(), key=lambda value: value[1], reverse=True)
pprint(char_frequency_sorted[0])
