def orth_triangle(cathetus1=0, cathetus2=0, hypotenuse=0) -> float | None:
    
    if (cathetus1 == 0 and cathetus2 > 0 and hypotenuse > 0 and hypotenuse > cathetus2):
        cathetus1 = (hypotenuse*hypotenuse - cathetus2*cathetus2) ** (1/2)
        return cathetus1
    
    elif (cathetus1 > 0 and cathetus2 == 0 and hypotenuse > 0 and hypotenuse > cathetus1):
        cathetus2 = (hypotenuse*hypotenuse - cathetus1*cathetus1) ** (1/2)
        return cathetus2
    
    elif (cathetus1 > 0 and cathetus2 > 0 and hypotenuse == 0):
        hypotenuse = (cathetus1*cathetus1 + cathetus2*cathetus2) ** (1/2)
        return hypotenuse
    
    else:
        return None 
       
C:\Git\Sajgakova\2024.11.10>python -i 6.py
>>> orth_triangle(cathetus1=3, hypotenuse=5)
4.0
>>> orth_triangle(cathetus1=8, cathetus2=15)
17.0
>>> print(orth_triangle(cathetus2=9, hypotenuse=3))
None
>>>