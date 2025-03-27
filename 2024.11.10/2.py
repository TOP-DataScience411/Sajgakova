def taxi_cost(length: None, time=0) -> int :

   if length is None or length < 0:
       return None
   if time < 0:
       return None       
       
   if length == 0:
       return 160 + time * 3  

   total_cost = (length * 6 / 150) + 80 + time * 3   
   return round(total_cost)


#>>> print(taxi_cost(-300))
#None
#>>> taxi_cost(1500)
#140
#>>> taxi_cost(2560)
#182
#>>> taxi_cost(0, 5)
#175
#>>> taxi_cost(42130, 8)
#1789