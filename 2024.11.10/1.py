def strong_password(password):
    if len(password) < 8:
        return False
    
    digit_count = 0
    upper = False
    lower = False
    symbol = False

    for char in password:
        if char.isdigit():
            digit_count += 1
        elif char.islower():
            lower = True
        elif char.isupper():
            upper = True
        elif not char.isalnum():
            symbol = True

    return (digit_count >= 2 and upper and lower and symbol)
    
#C:\Git\Sajgakova\2024.11.10>python -i 1.py
#>>> strong_password('password')
#False
#>>> strong_password('aP3:kD_l3')
#True