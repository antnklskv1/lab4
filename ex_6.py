#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = sys.argv[1]
# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(data):
    return sorted(list(unique(field(data, 'job-name'), ignore_case=True)), key=str.lower)

@print_result
def f2(f1):
    return list(filter(lambda s: (s.startswith('программист') or s.startswith('Программист')), f1))

@print_result
def f3(f2):
    return list(map(lambda x: x + ' с опытом Python', f2))

@print_result
def f4(f3):
    zp = [', зарплата ' + str(x) + ' руб.' for x in gen_random(100000, 200000, len(f3))]
    return ['{0}{1}'.format(a, b) for a, b in zip(f3, zp)]


with timer():
    f4(f3(f2(f1(data))))
