class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print("I am eating"+self.name)

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

def two_sum(num1,num2):
    num3 = num1
    num4 = num2
    num5 = num3 + num4
    print(num1,"+",num2,"=",num5)
    return num5

def test():
    a = 3
    b = -2
    c = 1.1
    print(float(a),abs(b),max(a,b),min(a,b),round(c),pow(3,4))
    print("hello world")
    print(two_sum(1,2))
    one = Person("老王", 1)
    one.eat()