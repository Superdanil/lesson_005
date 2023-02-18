# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код


from district.central_street.house1 import room1 as room11
from district.central_street.house1 import room2 as room12
from district.central_street.house2 import room1 as room21
from district.central_street.house2 import room2 as room22
from district.soviet_street.house1 import room1 as room31
from district.soviet_street.house1 import room2 as room32


print(f'На районе живут:{*room11.folks, *room12.folks, *room21.folks, *room22.folks, *room31.folks, *room32.folks}')
