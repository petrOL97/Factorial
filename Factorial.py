def factorial_tail_zeros_count(n):
    count = 0
    while(n > 0):
        n = n // 5
        count = count + n
    return(count)

try:
    n = int(input())
    if n<0:
        print("You can't use negative number")
    else:
        print(factorial_tail_zeros_count(n))
except ValueError:
    print('Invalid Value')

    
