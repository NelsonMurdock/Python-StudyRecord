class Person:
    c = "hh"

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        pass

    def eat(self, food):
        print(self.name + "爱吃" + food)

    pass


person = Person("谭卓杰", "男", "22")
print(person.name, person.age, person.sex)
person.eat("橘子")
