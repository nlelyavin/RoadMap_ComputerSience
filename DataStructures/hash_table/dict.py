"""Реализация HashTable - Dict"""

# Init
dict_1 = dict()

# set value
dict_1['item_1'] = 1

# get
value = dict_1.get('item_1')
print(f'{value=}')

# pop
dict_1['temp'] = 'temp'
temp = dict_1.pop('temp')
print(f'{temp=}')

# copy - Создает новый dict_2 (копию dict_1). dict_2 ссылается на другой объект в памяти, нежели dict_1
dict_2 = dict_1.copy()
print(f'{id(dict_2)} != {id(dict_1)}')

# clear - Полная отчистка словаря
dict_2.clear()
print(f'{dict_2=}')

# keys
keys = dict_1.keys()  # -> dict_keys(['item_1'])
print(f'{keys=}')

# values
values = dict_1.values()  # -> dict_values([1])
print(f'{values=}')

# update
dict_1.update({'update': 1})  # -> None. {'item_1': 1, 'update': 1}
print(f'{dict_1=}')

# items - возвращает tuple(key, value)
items = dict_1.items()  # -> dict_items([('item_1', 1), ('update', 1)])
print(f'{items=}')

# fromkeys.
dict_1.fromkeys([1, 2, 3], 2)
print(f'{dict_1=}')

# setdefault
default_value = dict_1.setdefault('default', 'default_value')
value = dict_1.setdefault('item_1', 'default_value')
print(f'{default_value=}', f'{value=}')

# popitem - LIFO
item = dict_1.popitem()
print(item)
