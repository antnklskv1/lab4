# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        if type(items) == list:
            self.items = items
        else:
            self.items = list(items)
        if len(kwargs) == 0:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs['ignore_case']

        i = 0
        while i < len(self.items):
            j = i+1
            while (j >= i) and (j < len(self.items)):
                if self.items[i] == self.items[j]:
                    self.items.pop(j)
                    j -= 1
                elif (type(self.items[i]) == str) and (type(self.items[j] == str)) and self.ignore_case:
                    a = str(self.items[i]).lower()
                    b = str(self.items[j]).lower()
                    if a == b:
                        self.items.pop(j)
                        j -= 1
                j += 1
            i += 1
        self.index = -1

    def __next__(self):
        if self.index == len(self.items)-1:
            raise StopIteration
        else:
            self.index += 1
            return self.items[self.index]

    def __iter__(self):
        return self

