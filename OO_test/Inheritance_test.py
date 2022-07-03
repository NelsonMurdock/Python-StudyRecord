class Animal:
    def eat(self):
        print("吃")
        pass

    def drink(self):
        print("喝")
        pass


class Dog(Animal):  # 继承
    def wwj(self):
        pass

    pass


class Cat(Animal):
    def mmj(self):
        pass

    pass


d1 = Dog()
d1.eat()
