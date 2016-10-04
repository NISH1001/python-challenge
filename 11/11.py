from PIL import Image

original = Image.open("cave.jpg", "r")
even = Image.new('RGB', original.size)
odd = Image.new('RGB', original.size)


for x in range(0, original.size[0],2):
    for y in range(0, original.size[1],2):
        odd.putpixel((x,y), original.getpixel((x,y)))
        even.putpixel( (x+1,y+1), original.getpixel((x+1, y+1)) )

even.show()
odd.show()
