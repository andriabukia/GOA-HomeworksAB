# "vashli", 29, 29.2, True False

list = ["luka", True , 12, 22.3]
#         0     1     2    3
x =  int(input("შემოიყვანეთ ელემენტი რომელსაც წაშლით "))



if x>=0 and x<len(list):
    list.remove(list[x])
    print(list)
else:
    print("invalid choice")


#დამატება
# .append list + num
# list.append(num)
# print(list[5])


#წაშლა
# .remove list - num
# list.remove(num)
# print(list)

#სიგრძე
#len() - length 
