import random
import datetime

# Напишите функцию (F): на вход список имен и целое число N;
# на выходе список длины N случайных имен из первого списка
# (могут повторяться, можно взять значения: количество имен 20,
# N = 100, рекомендуется использовать функцию random);


random_list = ['Kate', 'Jake', 'Mark', 'Jacov', 'Robert']
temp_names = []
for i in range(1, 21):
    temp_names.append(random.choice(random_list))


def f(names, n):
    for j in range(1, n):
        names.append(random.choice(temp_names))
    return names


func = f(temp_names, 100)
print(func)


# Напишите функцию вывода самого частого имени из списка на выходе функции F


def usually(prev_names):
    sort_names = list(prev_names)
    temp = {}
    for i in sort_names:
        temp[i] = sort_names.count(i)
    sort_list = list(temp.items())
    sort_list.sort(key=lambda j: j[1])
    sort_list.reverse()
    print(sort_list[0][0])


usually(func)


# Напишите функцию вывода самой редкой буквы,
# с которого начинаются имена в списке на выходе функции F

def rarely(prev_names):
    sort_names = list(prev_names)
    letter = []
    temp = {}
    for i in sort_names:
        letter += i[0]
    for i in letter:
        temp[i] = letter.count(i)
    sort_list = list(temp.items())
    sort_list.sort(key=lambda j: j[1])
    print(sort_list[0][0])


rarely(func)


# В файле с логами найти дату
# самого позднего лога (по метке времени):


file = open('log', encoding='utf-8')
max = datetime.datetime(1950, 1, 1)
for time in file:
    log = datetime.datetime.strptime(time[:23], '%Y-%m-%d %H:%M:%S,%f')
    if max < log:
        max = log
        time_max = time
print(time_max)
