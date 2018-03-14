
tuple1 = (1, 3, 5, 7)
tuple2 = 2, 4, 6, 8

list1 = [1, 3, 5, 7, 9]


def printList1(printName, printList):
    print(printName, printList, type(printList))
    for i in printList:
        print(i)


def printList(printName, printList):
    print(printName, printList, type(printList))
    for i in range(len(printList)):
        print('index=', i, 'value=', printList[i])


printList('tuple1', tuple1)
printList('tuple2', tuple2)
printList('list1', list1)

list1[1] = 2

printList('list1', list1)

list1.append(10)
print(list1)

list1.insert(1, 11)
print(list1)

list1.insert(-1, 12)
print(list1)

list1.remove(12)
print(list1)

print(list1[3:-1])
print(list1.index(11))
print(list1.count(11))

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

dir1 = {'key2': 'value1', 'key1': 'value2', 'key3': 'value3',
        'key1': 'value11', 'key5': printList, 'key6': list1}
print(dir1)

dir1['key5']('key5 test', list1)

dir1[11] = 'value4'
print(dir1)

del dir1['key1']
print(dir1)

d1 = {'apple': 1, 'pear': 2, 'orange': 3}
print(d1, d1['pear'])
