import zipfile
import re

zipped  = zipfile.ZipFile("channel.zip","r")
value = "90052"
out = ""
while True:
    data = zipped.read(value + ".txt")
    zipinfo = zipped.getinfo(value+".txt")
    print(zipinfo.comment)
    num = re.findall(r'\d+', str(data))
    if num:
        value = ''.join(num)
        out += (zipinfo.comment).decode("utf-8")
        print(value)
    else:
        print(data)
        break
print(out)

