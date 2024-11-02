num = int(input("Введите трехзначное число: "))

summ = 0
pr = 1

for _ in range(3):
    dig = num % 10
    summ += dig
    pr *= dig
    num //= 10

# Выводим результаты

print(f"Сумма цифр = {summ} \nПроизведение цифр = {pr}")
