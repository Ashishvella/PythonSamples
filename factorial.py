"""def fact(x):
    i=1
    res=0
    
    while i < x:
        res=x*i
        i=i+1
    return res"""
#above is while loop representation

def fact(x):
    i=1
    res=0

    for i in range(1,x):
        res=x*i
    return res
    



a=input("Enter any number");
print fact(a)

