list = ["ვაშლი", "მსხალი", "კიტრი"]
print("1. პროდუქტის დამატება.")
print("2. პროდუქტის წაშლა.")
print("3. პროდუქტების რაოდენობის გაგება.")

num1 = int(input("შემოიყვანე რიცხვი "))

if num1==1:
    product = input("შემოიყვანეთ პროდუქტი ")
    list.append(product)
    print(list)
elif num1 ==2:
    product = input("შემოიყვანეთ პროდუქტი ")
    list.remove(product)
    print(list)
elif num1==3:
 print(len(list))
else: print("invalid choice")