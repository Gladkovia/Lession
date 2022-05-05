import colorama
from colorama import Fore, Back, Style

colorama.init()

print(Fore.BLACK)
print(Back.GREEN)
what = input( "Что делаем (+, -):" )
print(Back.RED)
a = float(input("Введи первое чило: ") )
print(Back.CYAN)
b = float(input("Ввиди второе число: ") )

print(Back.YELLOW)
if what == "+":
    c = a + b
    print("Результат " + str(c))
elif what == "-":
    c = a - b
    print("Результат " + str(c))
else:
    print("Нет такого значения")
