min = int(input("Введите количество минут: "))

hours = min // 60
re_min = min % 60

print(f"{min} мин - это {hours} час {re_min} мин")
