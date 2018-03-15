import copy

a = [1, 2, 3]
b = a

print('--->1')
print('a-->', id(a), a)
print('b-->', id(b), b)

b[1] = 5
print('--->2')
print('a-->', id(a), a)
print('b-->', id(b), b)

b.sort()
print('--->3 sort')
print('a-->', id(a), a)
print('b-->', id(b), b)

a[2] = [4, 5, 6]
c = copy.copy(a)
print('--->4 copy')
print('a-->', id(a), a)
print('b-->', id(b), b)
print('c-->', id(c), c)

c[2] = 7
print('--->5 ')
print('a-->', id(a), a)
print('b-->', id(b), b)
print('c-->', id(c), c)

d = copy.deepcopy(a)
print('--->6 deepcopy')
print('a-->', id(a), a)
print('b-->', id(b), b)
print('c-->', id(c), c)
print('d-->', id(d), d)
