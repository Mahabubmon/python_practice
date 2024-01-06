class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)


print(p1.name)
print(p1.age)
        


def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("Asad",36)

print(p1)

def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Rahul",29)
p1.myfunc()