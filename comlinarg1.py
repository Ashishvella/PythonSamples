import sys
i=0
while(i<len(sys.argv)):
    if(sys.argv[i].isdigit()):
        print sys.argv[i]
    i+=1
