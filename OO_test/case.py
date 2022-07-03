class Character:
    def __init__(self, name):
        self.name = name
        print("hhh")
        pass

    def __del__(self):
        print("析构")
        # 主要是操作对象释放
        pass
