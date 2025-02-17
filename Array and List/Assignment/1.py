from array import *
a = array('i', [30, 40, 10, 20])
# access the element

# from the index
for i in range(4):
    print(a[i], end=' ')
print()
i = 0

while(i<len(a)):
    print(a[i], end=" ")
    i+=1
print()

# from the array
for x in a:
    print(x) 

# sorting of array

# # Convert array to list, sort the list, and convert it back to array
a_list = list(a)
print(f"max element of the list is: {max(a_list)}")
print(f"min element of the list is: {min(a_list)}")
a_list.sort()
a = array('i', a_list)
for i in a:
    print(i)


from numpy import *
b=array([2,7,8,3,4])
print(sort(b))
# 2D array
c=array([[2,7,8,3,4], [5,8,2,9,0]])
print(c[1][3])