num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

if num1 > 0 and num2 > 0:
    print("ორივე რიცხვი დადებითია")
elif num1 > 0 or num2 < 0:
    print("ერთ-ერთი რიცხვი დადებითია")
elif num1 < 0 and num2 > 0:
    print("ერთ-ერთი რიცხვი დადებითია")
else:
    print("ორივე რიცხვი უარყოფითია")