a=(12,23,12,2,21)
b=[12,23,34,44]
c={'x':12,'y':12,'z':3}
print type(a)
print type(b)
print type(c)

del a
del b[1]
del c['y']

#print a
print b
print c
b.append(12)
print b
