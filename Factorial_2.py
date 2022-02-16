def count_of_factorial_tail_zeros(n: int):
    ''' Return count of zeros at the end of factorial's value'''
    if not isinstance(n, int):
        raise TypeError("Input value type must be INT")
    if n < 0:
        raise ValueError("You can't use negative number")
    count = 0
    while n > 0:
        n = n // 5
        count += n
    return count

print(count_of_factorial_tail_zeros(input()))
