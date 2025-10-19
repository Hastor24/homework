print("Введите количество учебных дней (не больше 7):")
days = input()

if days.isdigit():
    days = int(days)

    if days < 1 or days > 7:
        print("количество дней должно быть от 1 до 7.")
    else:
        total_hours = 0

        print("Введите количество часов за 1 день:")
        h1_input = input()
        if h1_input.isdigit():
            h1 = int(h1_input)
            if h1 >= 0:
                total_hours = total_hours + h1
            else:
                print("количество часов не может быть отрицательным.")
        else:
            print("введите число.")

        if days >= 2:
            print("Введите количество часов за 2 день:")
            h2_input = input()
            if h2_input.isdigit():
                h2 = int(h2_input)
                if h2 >= 0:
                    total_hours = total_hours + h2
                else:
                    print("количество часов не может быть отрицательным.")
            else:
                print("введите число.")

        if days >= 3:
            print("Введите количество часов за 3 день:")
            h3_input = input()
            if h3_input.isdigit():
                h3 = int(h3_input)
                if h3 >= 0:
                    total_hours = total_hours + h3
                else:
                    print("количество часов не может быть отрицательным.")
            else:
                print("введите число.")

        print("Общее количество часов учебы:", total_hours)

else:
    print("Ошибка: введите число от 1 до 7.")
