from statistics import median, mean, geometric_mean, harmonic_mean
import math

        #'median' — медиана
        #'arithmetic' — среднее арифметическое
        #'geometric' — среднее геометрическое
        #'harmonic' — среднее гармоническое
    

def central_tendency(numb1: float, numb2:float, *numbers: float):
    
    new_numbers = (numb1, numb2) + numbers
    sorted_numbers = sorted(new_numbers)
    
    #Для проверки
    med = median(sorted_numbers)
    arithm = mean(sorted_numbers)
    geomet = geometric_mean(sorted_numbers)
    harm = harmonic_mean(sorted_numbers)
    print(f"'median': {med}, 'arithmetic': {arithm}, 'geometric': {geomet}, 'harmonic': {harm}\n")
    
    #Медиана
    if len(sorted_numbers)%2 == 0:
        index = (int(len(sorted_numbers)/2-1), int(len(sorted_numbers)/2))
        med1 = float((sorted_numbers[index[0]] + sorted_numbers[index[1]]) / 2)
    else:
        med1 = float(sorted_numbers[len(sorted_numbers)//2])
    
    #Среднее арифметическое
    arithm1 = float(sum(sorted_numbers)/len(sorted_numbers))
    
    #Среднее геометрическое
    geomet1 = math.prod(sorted_numbers)**(1/len(sorted_numbers))
    
    #Cреднее гармоническое
    reciprocals_sum = sum(1/x for x in sorted_numbers)
    harm1 = len(sorted_numbers)/ reciprocals_sum
    
    print(f"'median': {med1}, 'arithmetic': {arithm1}, 'geometric': {geomet1}, 'harmonic': {harm1}")
    
#C:\Git\Sajgakova\2024.11.10>python -i 5.py
#>>> central_tendency(1, 2, 3, 4)
#'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.2133638394006434, 'harmonic': 1.92
#
#'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.92
#>>> sample = 1, 2, 3, 4, 5
#>>> central_tendency(*sample)
#'median': 3, 'arithmetic': 3, 'geometric': 2.6051710846973517, 'harmonic': 2.18978102189781
#
#'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781
#>>> ^Z