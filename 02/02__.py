from collections import defaultdict

file = open("text.txt")

dict = defaultdict(int)

for line in file:
	for character in line:
		dict[character] += 1

for key in dict:
	if dict[key]>1:
		continue
	print(key + ": " +  str(dict[key] ) )

#print(dict)