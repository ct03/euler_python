#euler problem 1

def multiples(x):
    sum = 0
    for i in range (1,x):
        if i%3 == 0 or i%5 == 0:
            sum +=i
    print(sum)
    
multiples(1000)
