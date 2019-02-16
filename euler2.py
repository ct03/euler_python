#euler problem 2

x,y,z,sum,i = 1,2,0,0,0

while sum < 4000000:
    if i == 0:
        z=1
    elif i ==1:
        z=2
    else:
        z = x+y
        x=y
        y=z
    if z%2 == 0:
        sum+=z
    i+=1
    
print(sum)
        
        
