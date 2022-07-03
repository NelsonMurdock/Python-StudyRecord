class Animal:
    name = "tzj"

    def Say(self):
        print("我是动物")
        pass

    pass


class Duck(Animal):
    def Say(self):
        print("我是一只鸭子")
        pass

    pass


class Dog(Animal):
    def Say(self):
        print("我是一只狗")
        pass

    pass


def commomInvoke(obj):
    obj.Say()


dog1, duck1 = Dog(), Duck()
# duck1.Say()
# dog1.Say()

# listObj = [Duck(), Dog()]
# for item in listObj:
#     commomInvoke(item)

dog1.name = "hhh"
print(dog1.name)
print(duck1.name)
Animal.name = "lll"
print(dog1.name, duck1.name, Animal.name)
duck1.name = "www"
print(dog1.name, duck1.name, Animal.name)
