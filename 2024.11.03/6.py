ticket_number=input("Введите номер билета, чтобы узнать счасливый он или нет: ")
if len(ticket_number) == 6:
    sum_first_half = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
    sum_second_half = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
    if sum_first_half == sum_second_half:
        print("да")
    else:
        print("нет")
else:
    print("Неверный ввод. Пожалуйста, введите 6 цифр.")

#Введите номер билета, чтобы узнать счасливый он или нет: 183534
#да
#C:\Git\курсы\Sajgakova\2024.11.03>python 6.py
#Введите номер билета, чтобы узнать счасливый он или нет: 401367
#нет
