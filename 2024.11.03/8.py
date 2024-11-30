n = int(input("Введите число: "))
a, b = 1, 1
if n == 1:
    print(a)
else:
    print(a, end=' ')
    print(b, end=' ')
    for i in range(n-2):
        a, b = b, a + b 
        print(b, end=' ') 

#Введите число: 17
#1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
#C:\Git\курсы\Sajgakova\2024.11.03>python 8.py
#Введите число: 1
#1
