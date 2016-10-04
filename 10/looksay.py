
def sequence(a):
    x = str(a)
    if len(x) == 1:return "1"+x
    last, x, count , res, other = x[0], x[1::], 1, "", False
    for index, elem  in enumerate(x):
        if elem == last:
            count += 1
        else:
            other = True
            res += str(count) + last
            count = 1
            last = elem
    if not other:
        return str(count) + last
    if len(res) != 0:
        res += str(count) + last
    return res

def main():
    x = '1'
    for i in range(8):
        print(x)
        x = sequence(x)

if __name__=="__main__":
    main()
