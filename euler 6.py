#euler problem 6

def sumofsq(n):
    x = 0
    for i in range(1,n+1):
        x += i**2
    return(x)

def sqofsum(n):
    x=0
    for i in range(1,n+1):
        x +=i
    return(x**2)


    
print(sqofsum(100)-sumofsq(100))
