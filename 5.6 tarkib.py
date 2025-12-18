import math
import random

def math_operation():
    print("عمليات رياضيmathبا/n")
    print("1.ريشه دوم")
    print("2.توان")

    choice = input(":انتخاب کنيد")

    if choice == "1":
        num = float(input("عدد را وارد کنيد:"))
        if num<0:
            print("ريشه عدد منفي مجاز نيست")
        else:
            print("ريشه دوم:",math.sqrt(num))
    elif choice =="2":
        base = float(input("عدد پايه:"))
        exponent = float(input("توان:"))
        print("نتيجه:", math. pow(base,exponent))
    else:
        print("گزينه نامعتبر")


def random_math_exercise():
    number = random.randint(1,50)
    print("/nعدد تصادفي:",number)
    if number % 2 == 0:
        print("عدد زوج است")
        print("ريشه دوم:",math .sqrt(number))
    else:
         print("عدد فرد است")
         print("توان2:",math. pow(number,2))

def guess_game():
    secret = random.randint(1,100)
    attempts = 0
    print("/nبازي حدس عدد(1و100)")

    while True:
        guess = int(input("حدس بزن:"))
        attempts += 1
        if guess < secret:
            print("بزرگتره")

        elif guess > secret:
            print("کوچکتره")
        else:
            print(f"افرين عدد{secret}بود")
            print("تعداد تلاش ها:",attempts)
            break

def calculator():
    print("/nماشين حساب پيشرفته")
    print("1.جمع")
    print("2.تفريق")
    print("3.ضرب")
    print("4.تقسيم")
    print("5.توان")
    print("6.ريشه دوم")
    choice = input("انتخاب کنيد:")
    if choice in ["1","2","3","4","5",]:
        a = float(input("عدد اول:"))
        b= float(input("عدد دوم:"))

    if choice == "1":
        print("نتيجه:",a+b)
    elif choice == "2":
        print("نتيجه:",a-b)
    elif choice == "3":
        print("نتيجه:",a*b)
    elif choice == "4":
        if b == 0:
            print("تقسيم بر صفر مجاز نيست")
        else:
            print("نتيجه:",a/b)
    elif choice == "5":
         print (":نتيجه",math. pow(a,b))
    elif choice == "6":
        num = float(input("عدد را وارد کنيد:"))
        if num < 0:
         print("ريشه عدد منفي مجاز نيست")
        else:
         print("نتيجه:",math.sqrt(num))
    else:
        print("گزينه نامعتبر")

while True:
    print("/nبرنامه جمع بندي")
    print("1.عمليات math(ريشه و توان)")
    print("2.تمرين mathوrandom")
    print("3.بازي حدس عدد")
    print("4.ماشين حساب پيشرفته")
    print("5.خروج")
    choice = input("يک گزينه انتخاب کنيد:")
    if choice == "1":
        math_operations()
    elif choice == "2":
        random_math_exercise()
    elif choice == "3":
        guess_game()
    elif choice == "4":
        calculator()
    elif choice == "5":
        print("خداحافظ")
        break
    else:
        print("گزينه نامعتبر")
