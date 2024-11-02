miles1 = int(input("Введите целую часть миль: "))

miles2 = int(input("Введите дробную часть миль: "))

miles3 = miles1 + miles2 / 10

kil = miles3 * 1.61

r_kil = round(kil, 1)

print(f"{miles3} миль = {r_kil} км")
