
def testZip():
    a = [1, 2, 3]
    b = [4, 5, 6, 7, 8]

    ab = zip(a, b)

    print(list(ab))  # 需要加list来可视化这个功能

    for i, j in zip(a, b):
        print(i, j)


testZip()
