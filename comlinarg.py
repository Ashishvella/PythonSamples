import sys

print "Total arguments passed to the console", len(sys.argv)
print "The given values at command line are", sys.argv
print "The first parameter in command line is", sys.argv[0]
print "The type of value at first index is", type(sys.argv[1])
