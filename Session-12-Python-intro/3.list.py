my_list=[1,2,3,4,5,6,7]
print(my_list)
print("element at index 1: ",my_list[1])
my_list.append(8) #add new item
my_list[2]=33 #update value
print(my_list)
my_list.insert(0,20)
print("insert at 0",my_list)
my_list.remove(20) # remove by value
print(my_list)
my_list.pop() # default it will remove last element
my_list.pop(2) # remove element from index 2
print(my_list)
length= len(my_list)
print("Length: ",length)
print("Length: ",len(my_list))