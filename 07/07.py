from PIL import Image


oxygen = Image.open("oxygen.png","r")
height = oxygen.size[1]
width = oxygen.size[0]

y = int(height/2)-1
l = []
for i in range(0,width, 7):
    col = oxygen.getpixel((i,y))    
    if col[0] == col[1] == col[2] : 
        l.append(col[0])

print("".join([ chr(x) for x in l]))

ans = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print("".join([ chr(x) for x in ans]))
