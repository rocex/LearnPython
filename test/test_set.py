import logger

logger = Logger(logname='log.txt', loglevel=1, logger="fox").getlog()
logger.info('foorbar')

array = ['1', 'a', 'c', '0', '1', 0, 'c', 'b', 'z', '2', '1', 0]

string = 'Welcome to python world!'
logger.log(set(string))

unique_array = set(array)
print(unique_array)

unique_array.add('x')
print(unique_array)

unique_array.add('1')
print(unique_array)

print(unique_array.remove('1'))
print(unique_array)

print(unique_array.discard('2'))  # 和remove的区别是当不存在数据的时候不会报错
print(unique_array)

set1 = unique_array
set2 = ['c']

print(set1.difference(set2))  # 不同的元素
print(set1.intersection(set2))  # 相同的元素

unique_array.clear()
print(unique_array)
