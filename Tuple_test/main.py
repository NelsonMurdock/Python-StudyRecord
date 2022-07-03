_tuple = ("hello", 5, 1.5, [11, 22, 33], 1, 6, 8)
h = []
print(type(h))
print(type(_tuple))
print(_tuple)
print("--------------元组查询---------------")
print(_tuple.count(8))
print(_tuple.count(9))
print(_tuple[::-1])
print(_tuple[0:2])
"""for item in _tuple:
    print(_tuple)"""
print(_tuple[::-2])
print(_tuple[::-3])
print(_tuple[-2:-1])
# _tuple[0] = "0"错误的不可以修改
_tuple[3][0] = 0
print(_tuple)

_tuple1 = (1)  # 当元组中只有一个数据项的时候，必须要加上“，”
print(type(_tuple1))
_tuple2 = (1,)
print(type(_tuple2))
