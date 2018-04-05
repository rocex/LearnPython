
# 把形如
# cctv1,url1
# cctv1,url2
# cctv1,url3
# 格式的直播源合并成
# cctv1,url1#url2#url3

# 频道名词 英文逗号 源地址（如果同一个频道有多个源地址，用#号隔开）
# 例如： cctv1,http://www.cctv1.com#http://www.ccav1.com

readFileName = "C:\\tv.txt"
writeFileName = "C:\\tv2.txt"

result = {}


def readFile():
    with open(readFileName, 'r') as file:
        text2 = file.readlines()

        for item in text2:
            keyValue = item.split(",", maxsplit=1)

            if len(keyValue) < 2:
                continue

            if keyValue[0] in result:
                result[keyValue[0]] = result[keyValue[0]] + "#" + keyValue[1].replace("\n", "")
            else:
                result[keyValue[0]] = keyValue[1].replace("\n", "")

        # print(result)


def writeFile():
    with open(writeFileName, 'w') as file:

        keys = result.keys()

        for key in keys:
            line = key + "," + result.get(key)
            file.write(line+'\n')


readFile()
writeFile()
