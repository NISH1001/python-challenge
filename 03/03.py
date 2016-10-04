from collections import defaultdict
import re

file = open("data.txt")

dict = defaultdict(int)

text = ""

for line in file:
    text += line

test = re.findall(r'[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]', text)

out = ""
for word in test:
    print(word)
    out += word[4]

print(out)
