def factorial_tail_zeros_count(n):
''' Return count of zeros at the end of factorial's value'''
    if not isinstance(n, int):
        raise TypeError("Input value type must be INT")
        factorial_tail_zeros_count(n)
    if n < 0:
        raise ValueError("You can't use negative number")
    else:
        count = 0
        while(n > 0):
            n = n // 5
            count = count + n
        return(count) # comment

print(factorial_tail_zeros_count(input()))
