import copy
#ReferenceCopy

a=10
b=a
print "Address of a", id(a)
print "Address of b", id(b)

#DeepCopy-- any changes made to Original object do not reflect in the copy object.

list1=['Str1',1,'Str2',2.0,0xDDDD,1+5j]

print "Original list1", list1

list2=copy.deepcopy(list1)

print "Deep-copied list2", list2


list1.extend(['x','y','z'])

print "Original list1 after extend", list1
print "Deep-Copied list2 after extend", list2


print id(list1)
print id(list2)


#ShallowCopy-- any changes made to Original object do reflect in the copy object.

list3=copy.copy(list1)
print id(list1)
print id(list3)
list1.extend(['Deep1','Deep2','Deep3'])
print "Original list1 after extend", list1
print "Shallow-Copied list3 after extend", list3





