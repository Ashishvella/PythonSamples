fd=open('wipro.txt','w')
fd.write("First Line\n")
fd.write("second Line\n")
fd.write("third Line\n")
fd.write("Fourth Line\n")


fd.close()


print fd

fd1=open("wipro.txt",'r')
print fd1.readline()
fd1.close()
