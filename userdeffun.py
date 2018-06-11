def Function1(x,y):
    print "The result is ", x*y

def Function1(x,y):
    print "The result is", x+y
    return x+y
    
def Function2(x,y):
    print "The result is", x-y
    return x-y

print "Body's first line"
print Function1(2,3)
print Function2(3-2,5-4)
print "Back to main body"
