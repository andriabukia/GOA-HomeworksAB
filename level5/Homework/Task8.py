num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

if num1 % num2 == 0:
 print("იყოფიან ერთმანეთზე " + str(num1//num2))
else: print("არ იყოფიან ერთმანეთზე")