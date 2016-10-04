import pickle
f= open("banner.p","rb")
banner = pickle.load(f)
l = []
for item in banner:
    for x in item:
        l.append(x[0]*x[1])
        print(x)

    l.append("\n")

print(''.join(l))
'''
a = ["hello", "i am paradox"]
pickle.dump(a,open("test.p","wb"))
'''
