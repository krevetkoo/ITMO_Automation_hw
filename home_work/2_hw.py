def task_1() -> None:
    a = 10
    b = 3.14
    c = "meow"
    d = [1, 2, 3]
    e = True
    print("Тип a:", type(a))
    print("Тип b:", type(b))
    print("Тип c:", type(c))
    print("Тип d:", type(d))
    print("Тип e:", type(e))


task_1()


def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[0], a[1], a[2])


task_2()


def task_3(number: int) -> int:
    return number * number


print(task_3(5))