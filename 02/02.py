import re

file = open("text.txt")

for line in file:
	test = re.findall(r'[a-z]+', line)
	if not test:
		continue
	print(test)

