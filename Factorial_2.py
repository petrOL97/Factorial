def FactorialTailZerosCount(n):
        if type(n) != int:
                n=int(n)
        if n<0:
                return("You can't use negative number")
        else:
                count = 0
                while(n > 0):
                        n = n // 5
                        count = count + n
                return(count)
print(FactorialTailZerosCount(input()))

    
