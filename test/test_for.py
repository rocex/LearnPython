
index = 0


def log(msg):
    global index
    index += 1

    print("\n*****************", index, msg, "*****************")


log("test range(3)")
a = range(3)
print(a)

log("print loop array")
for i in a:
    print(i)

log("print range(1, 5, 2)")
for i in range(1, 5, 6):
    print(i)

log("print range(5)")
a = range(5)
print(a)

log("print loop range(5)")
while a:
    print(a[-1])
    a = a[:len(a) - 1]

log("print loop range(4)")
a = range(4)
print(a)

while a:
    print(a[0])
    a = a[1:len(a)]

print('index', index)
