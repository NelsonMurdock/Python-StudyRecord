# import sys
# print("参数个数为：",len(sys.argv[1:]))
# print("参数列表：",str(sys.argv[1:]))
import argparse

parse = argparse.ArgumentParser(prog="my - program", usage="(prog)s[options]usage",
                                description="my - description", epilog="my - epilog")
# 添加必选参数（位置参数）
parse.add_argument("name", type=str, help="你自己的名字")
parse.add_argument("age", type=str, help="你自己的年龄")
# 添加可选参数
parse.add_argument("-s", "--sex", type=str, help="你的性别")
result = parse.parse_args()  # 开始解析参数
print(result)  # 输入性别的时候要加-s
