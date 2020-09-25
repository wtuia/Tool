import sys
import os

print("输入你的文件(夹)路径(以当前路径为父路径):")
filePath = sys.stdin.readline()
filePath = filePath.strip()
if filePath.endswith("\\") or filePath.endswith("/"):
    filePath = filePath[0:len(filePath)-1]
name = ""
if filePath.find("."):
    name = filePath
    index = -1
    index1 = -1
    if filePath.find("\\") >= 0:
        index = filePath.rindex("\\")
    if filePath.find("/") >= 0 :
        index1 = filePath.rindex("/")
    index = max(index, index1)
    filePath = filePath[0:index]
if not os.path.exists(filePath):
    os.makedirs(filePath)
    print("文件夹"+filePath+"创建完成")
else:
    print("文件夹存在")
if not os.path.exists(name):
    fd = open(name, mode="w", encoding="utf-8")
    fd.close()
    print("文件"+name+"创建完成")
else:
    print("文件存在")
