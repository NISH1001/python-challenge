from PIL import Image

evil = open("evil2.gfx", "rb").read()

for i in range(5):
    open("image" + str(i)+".jpg", "wb").write(evil[i::5])

