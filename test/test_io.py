
fileName = "text.txt"


def writeFile():
    text = "this is first line.\nthis is second line.\nthis is third line.\n"

    try:
        print('\ntry write file')
        file = open(fileName, 'w')
        file.write(text)
    except Exception as ex:
        print('except write file--->', ex)
        raise RuntimeError('except write file--->') from ex
    finally:
        print('finally write file')
        file.close()


def appendFile():
    try:
        print('\ntry append file')
        file = open(fileName, 'a')
        file.write('this is append line.\n')
    except Exception as ex:
        print('except append file--->', ex)
    finally:
        print('finally append file')
        file.close()


def readFile():
    try:
        print('\ntry read file')
        file = open(fileName, 'r')
        text2 = file.read()
        print(text2)
    except Exception as ex:
        print('except read file--->', ex)
    finally:
        print('finally read file')
        file.close()


def readFileLine():
    try:
        print('\ntry read file line')
        file = open(fileName, 'r')
        text2 = file.readline()
        print(text2)

        text2 = file.readline()
        print(text2)
    except Exception as ex:
        print('except read file line--->', ex)
    finally:
        print('finally read file line')
        file.close()


def readFileLines():
    try:
        print('\ntry read file lines')
        file = open(fileName, 'r')
        text2 = file.readlines()

        print(text2)

        for item in text2:
            print(item)
    except Exception as ex:
        print('except read file lines--->', ex)
    finally:
        print('finally read file lines')
        file.close()


try:
    print('try')

    writeFile()

    appendFile()
    appendFile()

    readFile()

    readFileLine()

    readFileLines()

except Exception as ex:
    print('except write file--->', ex)
finally:
    print('finally\n')
