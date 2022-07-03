name = '谭卓杰'
classPro = '信息1803'
age = 22

print('我的名字是：%s 班级：%s,年龄：%d' % (name, classPro, age))
print('名字:{},年龄：{}'.format(name, age))
print('名字:{0}'.format(name))
print('名字:{0},年龄：{0}'.format(name, age))
# print('名字:{0},年龄：{}'.format(name, age))报错

name1 = input('请输入你的姓名：')
age1 = input('请输入你的年龄：')
print('age：%s' % age1)  # 默认接收str类型，受到数字类型要先转成int
# print('age：%d' % age1)报错
print(type(name1))
print(type(age1))
print('名字：{},年龄：{}'.format(name1, age1))
