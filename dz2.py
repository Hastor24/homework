#1
# age = int(input('введите ваш возраст:'))
# if age < 12:
#     print('Вы являетесь ребенком!')
#
# age2 = int(input('введите ваш возраст:'))
# if 12 <= age2 < 18:
#     print('Вы являетесь подростком!')
#
# age3 = int(input('введите ваш возраст:'))
# if 18 <= age3 < 60:
#    print('Вы являетесь взрослым!')
#
# age4 = int(input('введите ваш возраст:'))
# if age4 > 60:
#     print('Вы являетесь пенсионером!')
from itertools import count

#2
# num = int(input('введите ваше число от 0-9:'))
# if 0 <= num >= 9:
#     print('Введите корректное число в диапазоне от о-9')
# if num == 0:
#     print("Ваш символ на клавиатуре )")
# if num == 1:
#     print("Ваш символ на клавиатуре !")
# if num == 2:
#     print("Ваш символ на клавиатуре @")
# if num == 3:
#     print("Ваш символ на клавиатуре #")
# if num == 4:
#     print("Ваш символ на клавиатуре $")
# if num == 5:
#     print("Ваш символ на клавиатуре %")
# if num == 6:
#     print("Ваш символ на клавиатуре ^")
# if num == 7:
#     print("Ваш символ на клавиатуре &")
# if num == 8:
#     print("Ваш символ на клавиатуре *")
# if num == 9:
#     print("Ваш символ на клавиатуре (")

#3
# number = input("Введите трёхзначное число: ")
#
# if number.isdigit():
#     num = int(number)
#
#     if 100 <= num <= 999:
#         hundreds = num // 100
#         tens = (num // 10) % 10
#         units = num % 10
#
#         if hundreds == tens or hundreds == units or tens == units:
#             print("Есть одинаковые цифры")
#         else:
#             print("Все цифры разные")
#     else:
#         print("Это не трёхзначное число.")

#4
# number = input("Введите пятиразрядное число: ")
#
# if number.isdigit():
#     num = int(number)
#
#     if 10000 <= num <= 99999:
#         d1 = num // 10000
#         d2 = (num // 1000) % 10
#         d4 = (num // 10) % 10
#         d5 = num % 10
#
#         if d1 == d5 and d2 == d4:
#             print("Это палиндром.")
#         else:
#             print("Это не является палиндром.")

#5
# x = float(input("Введите координату x: "))
# y = float(input("Введите координату y: "))
#
# if x > 0:
#     if y > 0:
#         print("Точка в 1 четверти")
#     elif y < 0:
#         print("Точка в 4 четверти")
#     else:
#         print("Точка лежит на оси X")
# elif x < 0:
#     if y > 0:
#         print("Точка во 2 четверти")
#     elif y < 0:
#         print("Точка в 3 четверти")
#     else:
#         print("Точка лежит на оси X")
# else:
#     if y == 0:
#         print("Точка находится в начале")
#     else:
#         print("Точка лежит на оси Y")

# n = 8
# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print()

# for i in range (12):
#     if i ==5:
#         break]
# print (i)

# isham=True
# while isham:
#     if input('enter: ')=="stop":
#         isham=False
# будет выводиться ентер пока не введт стоп

# found=None
# for i in 'hello':
#     if i == "l":
#         found=True
#         break #выход если верно, если нет то..
    # else:
    #     found=False
    #     print(found)

# for i in range(1,12):
#     if i ==6:
#         break #- на 5 остановиться
#     print(i)

# i=5
# while i>15:
#     print(i)
#     i+=2
#прибавляют +2, выйдет 5,7,9,11,13


# nums=[5,7,2,4,7]
# nums[0]=7
# nums[1]=4
# nums[2]=2
# nums[3]=7
# nums[4]=5
# print(nums)