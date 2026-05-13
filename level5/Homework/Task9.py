age = int(input("შეიყვანეთ თქვენი ასაკი: "))
heartB = int(input("შეიყვანეთ თქვენი გულისცემა/პულსი : "))

if age<30 and heartB<140:
    print("შეგიძლიათ მეტი ივარჯიშოთ")
elif age>=30 and heartB>170:
    print("დასვენება გჭირდებათ")
else:
    print("აქტივობის დონე ნორმალურია")