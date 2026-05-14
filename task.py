list = ["vashli", "msxalo", 18]

print("1. პროდუქტების დამატება ")
print("2. პროდუქტების ამოშლა ")
print("3. სიგრძე ")

num = int(input("შემოიტანეთ რიცხვი "))

if num ==1:
    product = input("შემოიტანეთ პროდუქტი ")
    list.append(product)
    print(list)
elif num ==2:
    product = input("შემოიტანეთ პროდუქტი რომელსაც ამოშლით ")
    list.remove(product)
    print(list)
elif num ==3:
    print(len(list))
else:
    print("invalid choice")
