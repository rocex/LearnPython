# 根据视频地址把PotPlayer格式的播放列表(.dpl)去重,.dpl格式如下：
# 1*file*url1
# 1*title*cctv1
# 1*played*0/1
# 2*file*url2
# 2*title*cctv1
# 2*played*0/1
# 3*file*url3
# 3*title*cctv1
# 3*played*0/1

readFileName = "D:\\Program Files\\PotPlayer\\playlist\\直播源.dpl"
writeFileName = "D:\\Program Files\\PotPlayer\\playlist\\直播源-rd.dpl"


def readFile(readFileName, result):

    with open(readFileName, 'r', encoding='utf8') as file:
        text2 = file.readlines()

        for i in range(len(text2)):
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

            result[strFile] = strTitle

    return result


def writeFile(writeFileName, result):
    with open(writeFileName, 'w', encoding='utf8') as file:

        index = 1
        keys = result.keys()

        file.write("DAUMPLAYLIST\n")

        for key in keys:
            line = str(index) + "*file*" + key + "\n" + str(index) + "*title*" + result.get(key)
            file.write(line + '\n')
            index = index+1


def find(text, key):
    for i in range(len(text)):
        if text[i].startswith(key):
            return text[i]


result = {}
readFile(readFileName, result)
writeFile(writeFileName, result)
