
def funMap(x, y, z):
    return x + y + z


print(list(map(funMap, [1], [2], [3])))
print(list(map(funMap, [1, 2, 3], [4, 5, 6], [7, 8, 9])))
