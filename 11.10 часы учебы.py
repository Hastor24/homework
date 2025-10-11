while True:
    days_input = input("Введите количество учебных дней (от 1 до 7): ")

    if days_input.isdigit():
        days = int(days_input)
        if 1 <= days <= 7:
            break
        else:
            print("количество дней должно быть от 1 до 7.")
    else:
        print("введите целое число.")

total_hours = 0
day = 1

for i in range(days):
    while True:
        hours_input = input(f"Введите количество часов учебы в день {day}: ")
        try:
            hours = float(hours_input)
            if hours < 0:
                print("количество часов не может быть отрицательным.")
            else:
                total_hours += hours
                break
        except ValueError:
            print("введите число.")

    day += 1

print()
print("Результаты учебного времени:")
print(f"Количество учебных дней: {days}")
print(f"Общее количество часов за неделю: {total_hours:.2f}")