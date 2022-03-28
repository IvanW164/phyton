# Определить, присутствует ли в заданном списке строк, некоторое число 

import re
lst = ['yes', 'hello', '5 раз', '123']
signal = False
for i in range(len(lst)):
    if re.findall('[0-9]', lst[i]) != []:
        signal = True
print(signal)
