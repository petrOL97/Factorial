def FactorialTailZerosCount(n):
        if isinstance(n, int):
                if n<0:
                        return("You can't use negative number")
                else:
                        count = 0
                        while(n > 0):
                                n = n // 5
                                count = count + n
                        return(count)
        else:
                return('Invalid value')
                

print(FactorialTailZerosCount(int(input())))

    
