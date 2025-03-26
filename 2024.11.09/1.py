email = input().strip()

if "@" in email:
    atindex = email.index("@")
    if "." in email[atindex+1:]:
        print("да")
    else:
        print("нет")
else:
    print("нет")
    
    
    
#C:\Git\Sajgakova\2024.11.09>python -i 1.py
#sgd@ya.ru
#да

#C:\Git\Sajgakova\2024.11.09>python -i 1.py
#abcde@fghij
#нет