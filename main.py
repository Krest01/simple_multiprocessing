import multiprocessing
import random
import time


def data():
    dane = []
    for i in range(10):
        dane.append(random.randint(0, 1000))
    return dane

# Task 1


def suma_funkcja(dane):
    return sum(dane)


def chunks(lst, n):
    if len(lst) != 1:
        pool = multiprocessing.Pool(processes= len(lst))
        nlst = []
        for i in range(0, len(lst), n):
            nlst.append(lst[i:i + n])
        return chunks(pool.map(suma_funkcja, nlst), 2)
    else:
        print(f'Suma wszystkich liczb to {lst[0]}')

# Task 2


def minimum(dane):
    return min(dane)


def chunks_min(lst, n):
    if len(lst) != 1:
        pool = multiprocessing.Pool(processes= len(lst))
        nlst = []
        for i in range(0, len(lst), n):
            nlst.append(lst[i:i + n])
        return chunks_min(pool.map(minimum, nlst), 2)
    else:
        print(f'Najmniejszą liczbą jest {lst[0]}')

# task 3


def small_vowels(text):
    counter = 0
    for line in text:
        for char in line:
            if char in 'aeiou':
                counter += 1
    print(f"Liczba małych samogłosek to {counter}")
    return counter


def Big_vowels(text):
    counter = 0
    for line in text:
        for char in line:
            if char in 'AEIOU':
                counter += 1
    print(f'Liczba dużych samogłosek to {counter}')
    return counter


if __name__ == '__main__':
    dane = data()
    print(dane)
    time_s = time.perf_counter()
    chunks(dane, 2)
    chunks_min(dane, 2)
    with open('sample1.txt', 'r') as file:
        a = file.readlines()
    p3 = multiprocessing.Process(target=small_vowels, args=(a,))
    p4 = multiprocessing.Process(target=Big_vowels, args=(a,))
    tasks = [p3, p4]
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()
    time_f = time.perf_counter()
    print(f"Tasks finished in {time_f - time_s}")
