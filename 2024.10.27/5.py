miles1 = int(input("Введите целую часть миль: "))
miles2 = int(input("Введите дробную часть миль: "))

# ИСПРАВИТЬ: этот способ не сработает, если пользователю потребуется ввести дробную часть для числа с количеством десятичных знаков больше одного (см. тест ниже) — придумайте более универсальное решение
miles3 = miles1 + miles2 / 10

kil = miles3 * 1.61
r_kil = round(kil, 1)
print(f"{miles3} миль = {r_kil} км")



# ДОБАВИТЬ: скопированный из терминала результат выполнения программы с собственными данными, например:

# Введите целую часть миль: 5
# Введите дробную часть миль: 81
# 13.1 миль = 21.1 км
# КОММЕНТАРИЙ: должно быть
# 5.81 миль = 9.4 км


# ИТОГ: доработать — 2/5

