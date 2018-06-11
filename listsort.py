a=[12,23,45,12,4,5,7,8]

a.sort()
print a

a.sort(reverse=True)
print a



def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)

# print list
print('Sorted list:', random)
