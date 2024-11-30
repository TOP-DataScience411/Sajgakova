n=int(input("Введите целое число n: "))
sum=0
for i in range(1,n+1):
    if (n % i) == 0:
        sum += i
print(sum)

#C:\Git\курсы\дз3>python 3.py
#Введите целое число n: 50
#93