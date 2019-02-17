#euler problem 4
#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

y=0
z=[]
r=0

for i in range(999,100,-1):
    for k in range(999,100,-1):
        x = str((i*k)//1000)
        z = str(i*k)[-1]
        z += str(i*k)[-2]
        z += str(i*k)[-3]
        if x==z:
            if r<i*k:
                r=i*k

print(r)
