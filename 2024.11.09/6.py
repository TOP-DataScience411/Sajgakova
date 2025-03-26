number = input().strip()
binary = {'0', '1'}

if number.startswith('0b'):
    number = number[2:]
elif number.startswith('b'):
    number = number[1:]
    
for i in number[0:]: 
    if i not in binary:
        print("нет")
        exit()

print("да")


#C:\Git\Sajgakova\2024.11.09>python 6.py
#1b0101
#нет
