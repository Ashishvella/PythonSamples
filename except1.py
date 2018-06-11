
try:
    x=input("Enter first number")
    y=input("Enter second number")
    print "Division is", x/y
except ZeroDivisionError:
    print "Zero se Divide karega to Maar Khaega"
except NameError,e:
    print "Abe andha hai kya bhai. Variable define to karle"
    print e
except TypeError,e:
    print "Ek e type ka daal le bhai. Idhr rajnikant ni baitha"
    print e
else:
    print "Else is executed only when there is no error in the program"
finally:
    print "Finally will be executed all the times"
