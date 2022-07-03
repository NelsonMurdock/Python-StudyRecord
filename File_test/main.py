# 默认编码GBK
# f = open("./Test.txt", "w")
# # f = open("./Test.txt", "w", encoding="utf-8")改为以utf-8形式
# f.write("谭卓杰大帅比")  # 以GBK形式
# # f.write("sssss")  # 覆盖
# f.close()不关闭会造成内存泄漏

# f = open("Test.txt", "wb")  # 以二进制的形式
# f.write("ssssss".encode("utf-8"))
# f.close()

f = open("Test.txt", "r")
print(f.read())  # 读取所有

