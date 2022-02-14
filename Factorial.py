def FactorialTailZerosCount(n):
        count = 0
        while(n > 0):
            n = n // 5
            count = count + n
        return(count)
while (True):
    try:
        n = int(input())
        if n<0:
            print("You can't use negative number")
        else:
            print(FactorialTailZerosCount(n))
    except ValueError:
        print('Invalid Type')

    
