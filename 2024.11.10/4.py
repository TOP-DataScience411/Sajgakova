def countable_nouns(number: int, words: tuple[str, str, str]):
    if len(words) !=3:
        print("Картеж должен состоять из трёх слов")
    
    if (number%10  == 1):
        return words[0]
    elif ((number%10  == 2 or number%10  == 3 or number%10  == 4) and ( number%100 != 12 and number%100 != 13 and number%100 != 14)):
        return words[1]
    else: 
        return words[2]


#C:\Git\Sajgakova\2024.11.10>python -i 4.py
#>>> countable_nouns(1, ("год", "года", "лет"))
#'год'
#>>> countable_nouns(2, ("год", "года", "лет"))
#'года'
#>>> countable_nouns(10, ("год", "года", "лет"))
#'лет'
#>>> countable_nouns(12, ("год", "года", "лет"))
#'лет'
#>>> countable_nouns(22, ("год", "года", "лет"))
#'года'