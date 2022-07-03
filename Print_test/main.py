print(520)
print(92.5)

print("hello")
print('hello')

print(95 + 5)
print(100 / 20)
print(100 / 3)

fp = open('D:/Python/Code/Study Record/Print_test/Print.txt', 'a+')  # 如果文件不存在就创建，存在就在文件内容后面继续追加
print('hello', file=fp)  # 加上file是为了写入数据
fp.close()

print('hello', 'world')

print('hello\nworld')
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')  # hello被覆盖了
print('hello\bworld')  # 回退一个

print('https://www.baidu.com/')
# print('老师说：'大家好'')报错
print('老师说：\' 大家好 \'')

print(r'hello\nworld\\')  # 原字符，不希望字符串中的转义字符起作用，就使用原字符，在字符串前面加上R或者r
# print(r'hello\nworld\')  # 最后一个字符不能是单个反斜杠，可以是双斜杠
print("“”")

print(chr(0b100111001011000))
print(ord('谭'))
