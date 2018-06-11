def functioncall(x=0,y=0):
    print "The call of the functioncall is executed"
    print "The values passed are %d and %d" % (x,y)
    return x+y,x-y

print "Executing first line in Body"
x=0
y=0
functioncall()

print "The value of variables are %d and %d" %(x,y)

x=10
y=20
x,y=functioncall(x,y)

print "The values of variables are %d and %d" %(x,y)
