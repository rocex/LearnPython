a, b, c = 11, 2, 3

print(a, b, c)

if a < b < c:
    print("a < b < c")
else:
    print("a > b > c")

a, b = 1, 2

if a > b:
    print("a > b")
elif a == b:
    print("a == b")
else:
    print("a < b")

worked = True
# worked = False

print("done" if worked else "wrong")

if worked:
    print("true")
else:
    print("false")
