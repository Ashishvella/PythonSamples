x=input("Enter x value")
y=input("Enter y value")

if x>y and not x ==1 and not y==1:
    print "X is larger"
elif y>x and not y==1 and not x==1:
    print "Y is larger"
elif x==y:
    print "Both X and Y are equal"
else:
    print "Either X or Y have a 1 value"
