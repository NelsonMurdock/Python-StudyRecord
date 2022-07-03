import sys
import psutil
import os
import gc

# sys.getrefcount()
# a = []
# print(sys.getrefcount(a))  # 引用计数
# b = a
# print(sys.getrefcount(a))
# c = b
# print(sys.getrefcount(a))
# def showMeSize(tag):
#     pid = os.getpid()
#     p = psutil.Process(pid)
#     info = p.memory_full_info()
#     memory = info.uss / 1024 / 1024
#     print("{}memory used:{} MB".format(tag, memory))
#     pass
#
#
# def func():
#     showMeSize("初始化")
#     a = [i for i in range(10000000)]
#     b = [i for i in range(10000000)]  # 相互应用，引用数没有变为0
#     a.append(b)
#     b.append(a)
#     showMeSize("创建列表对象 a b 后")
#     # print(sys.getrefcount(a))
#     pass
#
#
# func()
# gc.collect()  # 手动释放
# showMeSize("完成时候的")
a = 100
b = 1000
print(id(a),id(b))
