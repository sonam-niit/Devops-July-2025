my_set={1,2,3,2,4,2,5} # unordered set
print(my_set) # you can see duplicates removed
my_set.add(10)
print("after add: ",my_set)
my_set.remove(10)# if element not present then throw error
print(my_set)
my_set.pop() # removes any random element
print(my_set)

my_set.discard(35)# if element present delete if not then leave it, not throwing error