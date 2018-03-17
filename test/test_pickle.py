import pickle

dict1 = {'b': 2, 'a': 1, 'c': [3, 4]}

print(dict1)

fileName = 'test_pickle.bin'

try:
    with open(fileName, 'wb') as file1:
        pickle.dump(dict1, file1)
except Exception as ex:
    print('exception->', ex)
finally:
    file1.close()

try:
    with open(fileName, 'rb') as file1:
        text = pickle.load(file1)
        print('reload file-->', text)
except Exception as e:
    raise
finally:
    pass