#euler problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

z = 0
i = 10
while z == 0:   
    if i%2 == 0 and i%3 == 0 and i%7 ==0 and i%11 == 0 and i%13 == 0 and i%17 ==0 and i%19 ==0:
        for k in range(4,21):
            if i%k == 0:
                z=1
            else:
                z=0
                break
        if z==1:
            break
    i+= 10

print(i)            
