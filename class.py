class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# p1 = Person("John", 36)


# print(p1.name)
# print(p1.age)
        


# def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("Asad",36)

# print(p1)

# def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("Rahul",29)
# p1.myfunc()


# class Person:
#     def __init__(mysillyobject, name, age):
#         mysillyobject.name = name
#         mysillyobject.age = age


#     def myfunc(abc):
#         print("Hello my name is " + abc.name)


# p1 = Person("Arif", 24)
# p1.myfunc()


# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname, year)
#         self.graduationyear = year

# # x = Student("Rahul","Al", 2019)
        
#     def welcome(self):
#       print("Welcome", self.fname, self.lname,"to the class of",
#             self.graduationyear)
        
class Mynumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            self.a += 1 
            return x 
        else:
            raise StopIteration
        
myclass = Mynumber()
myiter = iter(myclass)

for x in myiter:
    print(x)