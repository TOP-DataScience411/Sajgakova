sum = 0

for i in range(3):
    number = float(input(f"Введите число {i + 1}: "))  
    if number > 0:  
        sum += number  

print(sum)


#C:\Git\курсы\дз2>python 1.py
#Введите число 1: 4
#Введите число 2: -22
#Введите число 3: 1.5
#5.5