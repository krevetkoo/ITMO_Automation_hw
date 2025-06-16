def task_2(a,b):
    if a > b:
        print("Наибольшее число:", a)
    else:
        print("Наибольшее число:", b)
task_2(12,14)

def task_3(x,y):
    if x - y == 135 or y - x == 135:
        print("yes")
    else:
        print("No")
task_3(150, 15)

def task_4(month):
    if month == 12 or month == 1 or month == 2:
        print("зима")
    elif month == 3 or month == 4 or month == 5:
        print("весна")
    elif month == 6 or month == 7 or month == 8:
        print("лето")
    elif month == 9 or month == 10 or month == 11:
        print("осень")
    else:
        print("Неправильный месяц")
task_4(13)

def task_5(num1, num2, num3):
    if num1 > 10 and num2 > 10 and num3 > 10:
        print("yes")
    else:
        print("no")
task_5(20,16,30)
