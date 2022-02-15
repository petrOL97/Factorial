def factorial_tail_zeros_count(n):
    ''' Return count of zeros at the end of factorial's value'''
    if not isinstance(n, int):
        raise TypeError("Input value type must be INT")
    if n < 0:
        return("You can't use negative number")
    else:
        count = 0
        while(n > 0):
            n = n // 5
            count = count + n
        return(count)

print(factorial_tail_zeros_count(input()))

    
