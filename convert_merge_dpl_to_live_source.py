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

readFileName = "C:\\live.dpl"
writeFileName = "C:\\live.txt"

result = {}


def readFile():
    with open(readFileName, 'r') as file:
        text2 = file.readlines()

        iIndex = 1

        for i in range(len(text2)):
            keyFile = str(iIndex) + "*file*"
            blFind = text2[i].startswith(keyFile)

            print(str(i))

            if not blFind:
                continue

            strFile = text2[i].replace(keyFile, "", 1)

            keyTitle = str(iIndex) + "*title*"

            strTitle = text2[i+1].replace(keyTitle, "", 1).replace("\n", "")

            if strTitle in result:
                result[strTitle] = result[strTitle] + " # " + strFile.replace("\n", "")
            else:
                result[strTitle] = strFile.replace("\n", "")

            print(str(i) + "-->" + strTitle + "-->" + result[strTitle])

            iIndex += 1


def writeFile():
    with open(writeFileName, 'w') as file:

        keys = result.keys()

        for key in keys:
            line = key + ", " + result.get(key)
            file.write(line+'\n')


readFile()
writeFile()
