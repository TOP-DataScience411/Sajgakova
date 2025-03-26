fruits = []

while True:
    fruit = input("Введите фрукт: ").strip()
    if fruit == "":  
        break
    fruits.append(fruit) 


if len(fruits) == 0:
    result = ""  
elif len(fruits) == 1:
    result = fruits[0]  
else:
    result = ", ".join(fruits[:-1]) + " и " + fruits[-1]  

print(result)

#C:\Git\Sajgakova\2024.11.09>python -i 2.py
#Введите фруктыяблоко
#Введите фрукты
#яблоко
#>>> ^Z
#
#C:\Git\Sajgakova\2024.11.09>python -i 2.py
#Введите фрукты: яблоко
#Введите фрукты: груша
#Введите фрукты:
#яблоко и груша
#>>> ^Z
#
#C:\Git\Sajgakova\2024.11.09>python -i 2.py
#Введите фрукт: яблоко
#Введите фрукт: груша
#Введите фрукт: апельсин
#Введите фрукт:
#яблоко, груша и апельсин
#>>> ^Z

#C:\Git\Sajgakova\2024.11.09>python -i 2.py
#Введите фрукт: яблоко
#Введите фрукт: груша
#Введите фрукт: апельсин
#Введите фрукт: лимон
#Введите фрукт:
#яблоко, груша, апельсин и лимон
#>>> ^Z


