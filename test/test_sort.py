import time
import random
import copy


def sortBubble(array1):  # 冒泡排序
    current = time.time()
    print('pop sort')
    # print(array1)

    for i in range(0, len(array1)):
        for j in range(i + 1, len(array1)):
            if array1[i] > array1[j]:
                temp = array1[i]
                array1[i] = array1[j]
                array1[j] = temp

    # print(array1)
    print(abs(time.time() - current))


def sort1(array1):
    current = time.time()
    print('sort')
    # print(array1)

    array1.sort()

    # print(array1)
    print(abs(time.time() - current))


array = []


def initArray():
    global array

    for i in range(10000):
        array.append(random.randrange(1000))


initArray()

# print(array)

sort1(copy.deepcopy(array))
sortBubble(copy.deepcopy(array))
