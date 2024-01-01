# for x in "banana":
#     print(x) 

#text = "this is a goal"

#if "goal" in text:
   # print("yes,it is on it")
   # print("expensive" not in text)


#txt = "life is free"
#if "expensive" not in txt:
#   print("expensive, Not in the Sentence")

# a = "Hellow, World! "
# print(a.upper())
# print(a.lower())
# print(a.strip())
# print(a.replace("H","J"))
# print(a.split())

# b = "hell"
# c = "to"
# d = "go"

# e = a+" "+b+" "+c+" "+d
# print(e)



# price = 45
# item = 10
# quantity = 25

# mymarketting = "The price is:{}.The item:{}.The amount of quantity:{}"
# print(mymarketting.format(price,item,quantity))


# thisTuple = ("apple","Banana","Cherry")

# print(len(thisTuple))

# #tuple() constructor
# store = tuple(("Jinga","Potol","Alu","kochu","kodu","papaya"))
# print(store)
# print(store[1])
# print(store[2:5])
# print(store[:4])
# print(store[2:])
# print(store[-4:-1])

#update tuples

store = tuple(("Jinga", "Potol", "Alu", "kochu", "kodu", "papaya"))

y = list(store)
y[1] = "vendi"
store = tuple(y)

z = ("orange",)
store += z
z = list(store)
z.remove("Jinga")
store = tuple(z)

print(store)







