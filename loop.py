# road = ["posta","islambagh","lalbagh"]
# for i in road:
#     print(i)


place = ["azimpur","new_market","dhanmondi"]
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

newList = [x for x in place if "a" in x]
print(newList)