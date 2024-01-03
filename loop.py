# road = ["posta","islambagh","lalbagh"]
# for i in road:
#     print(i)


# place = ["azimpur","new_market","dhanmondi"]
# for x in range(len(place)):
#     print(place[x])



# i = 0 
# while i < len(place):
#     print(place[i])
#     i = i + 1



# [print(x) for x in place]

# newlist = []
# for x in place:
#     if "a" in x:
#         newlist.append(x)

#         print(newlist)

# newList = [x for x in place if "a" in x]
# print(newList)

# def myfunc(n):
#     return abs(n - 50)
# numberList = [100,50,25,23]
# numberList.sort(key = myfunc)
# print(numberList)

#access set items

place = {"azimpur","new_market","dhanmondi"}  
# for x in place:
#     print(x)

# print("azimpur" in place)

# place.add("asadget")

# road = {12,13,15,18}
# place.update(road)


# place.remove("new_market")

# del road

# print(road)



# print(place)

# x = place.intersection(road)

# print(x)

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1994

}
# x = thisdict["brand"]

# print(x)

# y = thisdict.keys()
# print(y)

# thisdict["color"] = "white"

# print(y)

thisdict.update({"year":2020})

print(thisdict)