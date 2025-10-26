import random

def gen_list(n, a, b):
    lst = []
    for i in range(n):
        lst.append(random.randint(a, b))
    return lst

def max_num(lst):
    m = lst[0]
    for x in lst:
        if x > m:
            m = x
    return m

def repeat_count(lst):
    c = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                c += 1
                break
    return c

def positives(lst):
    new = []
    for x in lst:
        if x > 0:
            new.append(x)
    return new

def remove_even(lst):
    new = []
    for x in lst:
        if x % 2 != 0:
            new.append(x)
    return new

def unique_two(a, b):
    new = []
    for x in a:
        if x not in new:
            new.append(x)
    for x in b:
        if x not in new:
            new.append(x)
    return new

a = gen_list(5, -5, 10)
b = gen_list(5, 0, 10)

print("A:", a)
print("B:", b)
print("Максимум A:", max_num(a))
print("Повторы A:", repeat_count(a))
print("Положительные из A:", positives(a))
print("Без четных из A:", remove_even(a))
print("Уникальные из A и B:", unique_two(a, b))
