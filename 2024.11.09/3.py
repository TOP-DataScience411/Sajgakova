
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

for i in range (len(list1)-len(list2)+1):
    if list2 == list1[i:i+len(list2)]:
        print("да")
        break
else:
    print("нет")


#C:\Git\Sajgakova\2024.11.09>python 3.py
#1 2 3 4
#1 2
#да

#C:\Git\Sajgakova\2024.11.09>python 3.py
#1 2 3 4
#2 4
#нет