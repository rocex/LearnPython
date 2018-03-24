array = ['1', 'a', 'c', '0', '1', 0, 'c', 'b', 'z', '2', '1', 0]

string = 'Welcome to python world!'
print(set(string))

unique_array = set(array)
print(unique_array)

unique_array.add('x')
print(unique_array)

unique_array.add('1')
print(unique_array)

unique_array.remove('1')
print(unique_array)


unique_array.clear()
print(unique_array)
