#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 4, 10)
data3 = ['a', 'A', 'b', 'BB', 'bB']
data4 = ['aaA', 'aAa', 'Aaa', 'b', 'c', 'C']
data5 = ['a', 'b', 'a', 'B']

# Реализация задания 2
print([x for x in Unique(data1)])
print([x for x in Unique(data2)])
print([x for x in Unique(data3, ignore_case=True)])
print([x for x in Unique(data4, ignore_case=True)])
print([x for x in Unique(data5)])

