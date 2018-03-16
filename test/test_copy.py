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
print('a-->', id(a), a, 'id(a[2])-->', id(a[2]), 'id(a[2][0])-->', id(a[2][0]))
print('b-->', id(b), b)
print('c-->', id(c), c, 'id(c[2])-->', id(c[2]), 'id(c[2][0])-->', id(c[2][0]))

c[2][0] = 9
print('--->5 copy')
print('a-->', id(a), a, 'id(a[2])-->', id(a[2]), 'id(a[2][0])-->', id(a[2][0]))
print('b-->', id(b), b)
print('c-->', id(c), c, 'id(c[2])-->', id(c[2]), 'id(c[2][0])-->', id(c[2][0]))

c[2] = 7
print('--->6 ')
print('a-->', id(a), a, 'id(a[2])-->', id(a[2]), 'id(a[2][0])-->', id(a[2][0]))
print('b-->', id(b), b)
print('c-->', id(c), c, 'id(c[2])-->', id(c[2]), '   id(c[2])-->', id(c[2]))


d = copy.deepcopy(a)
print('--->7 deepcopy')
print('a-->', id(a), a, 'id(a[2])-->', id(a[2]), 'id(a[2][0])-->', id(a[2][0]))
print('b-->', id(b), b)
print('c-->', id(c), c)
print('d-->', id(d), d, 'id(d[2])-->', id(d[2]), 'id(d[2][0])-->', id(d[2][0]))

d[2][0] = 99
print('--->8 deepcopy')
print('a-->', id(a), a, 'id(a[2])-->', id(a[2]), 'id(a[2][0])-->', id(a[2][0]))
print('b-->', id(b), b)
print('c-->', id(c), c)
print('d-->', id(d), d, 'id(d[2])-->', id(d[2]), 'id(d[2][0])-->', id(d[2][0]))
