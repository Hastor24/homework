import random

options = ["камень", "ножницы", "бумага"]

player_options = input("Выбери: камень, ножницы или бумага: ")
computer = random

print(f"Ты выбрал: {player_options}")
print(f"Компьютер выбрал: {computer}")

rules = {
    "камень": "ножницы",
    "ножницы": "бумага",
    "бумага": "камень"
}

if player_options == computer:
    print("Ничья!")
elif rules[player_options] == computer:
    print("Ты выиграл!")
else:
    print("Компьютер выиграл!")