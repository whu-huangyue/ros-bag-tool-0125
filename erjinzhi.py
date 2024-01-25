myfname="IMU"

f = open(myfname, "rb")

with open(myfname,"r",encoding="utf-8") as fd:   # 打开文件时指定编码为utf-8
    abytes=fd.read()                             # 用utf-8的方式读取二进制文件（实际上所有的文件存储形式都是二进制）
    print(abytes)

# with open(myfname,"rb") as fd:                   # 打开二进制文件
#     abytes=fd.read()                             # 读取二进制内容到字节串中
#     print(abytes)
#     print(abytes.decode("utf-8"))                # 二进制字节转为（翻译）字符