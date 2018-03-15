
def testZip():
    a = [1, 2, 3]
    b = [4, 5, 6, 7, 8]

    ab = zip(a, b,  b, a)

    print(list(ab))  # 需要加list来可视化这个功能

    ab = zip(a, b,  b, a)

    for i, j, k, l in ab:
        print(i, j, k, l)


testZip()
