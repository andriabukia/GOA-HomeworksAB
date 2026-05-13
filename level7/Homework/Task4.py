list = ["phone", 29, True, False, 512.3]
print(list)
num = int(input("enter id you want to delete "))
if num >4 or num<-3:
     print("invalid choice")
else: list.remove(list[num]) 
print(list)