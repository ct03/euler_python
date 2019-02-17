#euler problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def factor(n):
    p = 0
    for i in range(2,n):
        if n%i==0:
            if prime(i) == None:
                break
            p = prime(i)
    print(p)

                
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return
    return(n)
       
factor(600851475143)
