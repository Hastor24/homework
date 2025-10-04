import random
computer = random.randint(1, 3)

print("Выберите ход:")
print("1 — камень")
print("2 — ножницы")
print("3 — бумага")

user = int(input("Ваш выбор (1/2/3): "))

print()

if computer == 1:
    print("Компьютер выбрал: камень")
elif computer == 2:
    print("Компьютер выбрал: ножницы")
else:
    print("Компьютер выбрал: бумага")

if user == computer:
    print("Ничья!")
elif user == 1:
    if computer == 2:
        print("Вы выиграли!")
    else:
        print("Вы проиграли")
elif user == 2:
    if computer == 3:
        print("Вы выиграли!")
    else:
        print("Вы проиграли")
elif user == 3:
    if computer == 1:
        print("Вы выиграли!")
    else:
        print("Вы проиграли.")
else:
    print("Некорректный ввод.")
