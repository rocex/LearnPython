import copy

a = [1, 2, 3]
b = a

print(a, b)
print(id(a))
print(id(b))

b[1] = 5

print(a, b)
print(id(a))
print(id(b))

b.sort()
print(a, b)
print(id(a))
print(id(b))

c = copy.copy(a)
print(a, b, c)
print(id(a))
print(id(b))
print(id(c))


c[2] = 7
print(a, b, c)
print(id(a))
print(id(b))
print(id(c))
