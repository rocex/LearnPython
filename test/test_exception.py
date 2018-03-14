fileName = 'test1.txt'

file = None

try:
    file = open(fileName, 'r+')
except Exception as ex:
    print(ex)

    yn = input('create file(y/n)?')
    if yn == 'y':
        file = open(fileName, 'w')
else:
    file.write('test exception')
finally:
    file.close()
