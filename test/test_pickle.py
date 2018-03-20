import pickle

dict1 = {'b': 2, 'a': 1, 'c': [3, 4]}

print(dict1)


def writePickle(fileName):
    # with 语句会自动关闭文件，此处作为测试
    try:
        with open(fileName, 'wb') as file1:
            pickle.dump(dict1, file1)
    except Exception as ex:
        print('in exception, file closed? ', file1.closed)
        print('in exception->', ex)
    finally:
        print('in finally, file closed? ', file1.closed)
        file1.close()


def reloadPickle(fileName):
    try:
        with open(fileName, 'rb') as file1:
            text = pickle.load(file1)
            print('reload fileName-->', fileName, 'file content-->', text)
    except Exception as ex:
        print('in exception, file closed? ', file1.closed)
        print('in exception->', ex)
    finally:
        print('in finally, file closed? ', file1.closed)
        file1.close()


fileName = 'test_pickle.bin'

writePickle(fileName)
reloadPickle(fileName)
reloadPickle(fileName + '')
