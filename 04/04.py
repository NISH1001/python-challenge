import urllib.request
import re

link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

#num = 12345
num = 8022

#for i in range(400):
while(True):
    test = urllib.request.urlopen(link+str(num)).read()
    val = re.findall(r'\d+', str(test))
    if val:
        t = ''.join(val)
        num = int(t)
        print(num)
    else:
        print(test)
        break
