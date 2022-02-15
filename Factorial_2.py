def factorial_tail_zeros_count(n): # Здесь добавить тайп хинтинг. Передвинуть count в начало названия.
    ''' Return count of zeros at the end of factorial's value'''
    if not isinstance(n, int):
        raise TypeError("Input value type must be INT")
    if n < 0:
        return("You can't use negative number")
    else: # else после return не нужен
        count = 0
        while(n > 0): # скобки не нужны 
            n = n // 5
            count = count + n # можно воспользоваться оператором +=
        return(count) # скобки не нужны

print(factorial_tail_zeros_count(input()))

    
