fileName = 'test.txt'

file = None

try:
    print('1 in try')
    file = open(fileName, 'r+')
except Exception as ex:
    print('2 in exception', ex)

    yn = input('3 create file(y/n)? ')
    if yn == 'y':
        file = open(fileName, 'w')
else:
    print('4 in else, write file content')
    file.write('test exception')
finally:
    print('5 in finally')

    if file is None:
        print('6 not close file', file)
    else:
        print('7 close file')
        file.close()
