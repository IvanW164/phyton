spisok_1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
stroka_1 = "йцу"
count = 0
print(spisok_1.count(stroka_1))
if spisok_1.count(stroka_1) <2:
    count = -1
else:
    for i in range(len(spisok_1)):
        if spisok_1[i] == stroka_1:
            count+=1
            if count ==2:
                count = i
                break
print(f'Искомое {stroka_1}, ответ {count}')
