sum = 0
n=int(input("Введите целое число n: "))

for i in range(n):
    num = int(input("Введите целое число: "))  
    if num > 0:  
        sum += num  
    n=n-1
print(sum)

#C:\Git\курсы\дз3>python 2.py
#Введите целое число n: 6
#Введите целое число: 3
#Введите целое число: -5
#Введите целое число: 1
#Введите целое число: 10
#Введите целое число: -1
#Введите целое число: 8
#22
