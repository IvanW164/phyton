# Дано число обозначающее день недели. Вывести его название
# и указать является ли он выходным.
List = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вскр']
numb_day = int(input("введите число от 1 до 7...."))
if 0 < numb_day < 8:
    if numb_day <= 5:
        print(f'{list[numb_day - 1]} - будний день.')
    else:
        print(f'{list[numb_day - 1]} - выходной день.')
else:
    print('Введено число не имеющее соответствия с днем недели.')





#if numb_day <= 5:
    #print(f'{list[numb_day]} будний день')
#else:
    #print(f'{list[numb_day]} выходной день')

