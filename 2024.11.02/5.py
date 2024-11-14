a1 = input("Введите координаты первой клетки: ")
a2 = input("Введите координаты второй клетки: ")

letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
number=['1', '2', '3', '4', '5', '6', '7', '8']

if (letter.index(a1[0])==letter.index(a2[0]) or number.index(a1[1])==number.index(a2[1])):
    print('да')
else:
    print('нет')