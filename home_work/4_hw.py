class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
rect3 = Rectangle(8, 4)

print("Прямоугольник 1:")
print("Площадь:", rect1.calculate_area())
print("Периметр:", rect1.calculate_perimeter())

print("\nПрямоугольник 2:")
print("Площадь:", rect2.calculate_area())
print("Периметр:", rect2.calculate_perimeter())

print("\nПрямоугольник 3:")
print("Площадь:", rect3.calculate_area())
print("Периметр:", rect3.calculate_perimeter())


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print("Сложение:", self.a + self.b)

    def multiplication(self):
        print("Умножение:", self.a * self.b)

    def division(self):
        print("Деление:", self.a / self.b)

    def subtraction(self):
        print("Вычитание:", self.a - self.b)


math = Math(10, 5)
math.addition()
math.multiplication()
math.division()
math.subtraction()

class SidebarButton:
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.text}"
buttons = [
    SidebarButton("Text Box"),
    SidebarButton("Check Box"),
    SidebarButton("Radio Button"),
    SidebarButton("Web Tables"),
    SidebarButton("Buttons"),
    SidebarButton("Links"),
    SidebarButton("Broken Links - Images"),
    SidebarButton("Upload and Download"),
    SidebarButton("Dynamic Properties")
]

for button in buttons:
    print("\n" + button.text)
    print("Тип:", button.type)
    print(button.click())
