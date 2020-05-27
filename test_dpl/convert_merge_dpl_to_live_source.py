# 把PotPlayer格式的播放列表(.dpl)转换&合并成HDP支持的格式(.txt),.dpl格式如下：
# 1*file*url1
# 1*title*cctv1
# 1*played*0/1
# 2*file*url2
# 2*title*cctv1
# 2*played*0/1
# 3*file*url3
# 3*title*cctv1
# 3*played*0/1
# 合并成如下格式，以方便导入hdp、直播狗、小薇直播等app中
# cctv1,url1#url2#url3

# 频道名词 英文逗号 源地址（如果同一个频道有多个源地址，用#号隔开）
# 例如： cctv1,http://www.cctv1.com#http://www.ccav1.com

from datetime import date
from pathlib import Path

readDirName = "D:\\Program Files\\PotPlayer\\playlist\\"
writeDirName = "C:\\live\\" + str(date.today()) + ".txt"


def readFile(readFileName, result):

    with open(readFileName, 'r', encoding='utf8') as file:
        text2 = file.readlines()

        for i in range(len(text2)):
            print("i-->" + str(i))

            keyFile = str(i) + "*file*"
            strFile = find(text2, keyFile)

            if not strFile:
                continue

            keyTitle = str(i) + "*title*"
            strTitle = find(text2, keyTitle)

            if not strTitle:
                continue

            strFile = strFile.replace("\n", "").replace(keyFile, "", 1)
            strTitle = strTitle.replace("\n", "").replace(keyTitle, "", 1)

            if strTitle in result:
                result[strTitle] = result[strTitle] + " # " + strFile
            else:
                result[strTitle] = strFile

            print("i-->[%d], [%s], [%s]" % (i, strTitle, strFile))

    return result


def writeFile(writeFileName, result):
    with open(writeFileName, 'w', encoding='utf8') as file:

        keys = result.keys()

        for key in keys:
            line = key + ", " + result.get(key)
            file.write(line + '\n')


def find(text, key):
    for i in range(len(text)):
        if text[i].startswith(key):
            return text[i]


def test():
    path = Path(readDirName)

    result = {}

    files = list(path.glob('*.dpl'))

    for file in files:
        result = readFile(file, result)
        
    writeFile(writeDirName, result)


test()

# readFile()
# writeFile()
