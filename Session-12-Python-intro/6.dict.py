my_dict={
    "name":"sonam soni", 
    "age":45,
    "city":"mumbai",
    "expertise":["DevOps","JAVA FSD","MEAN","MERN","GenAI"]
}
# print(my_dict)
print("Name: ",my_dict["name"]) # name,age,city,expertise indexes
my_dict['manager']="Test Manager"
# print(my_dict)

#iterate one by one
for key in my_dict:
    if(isinstance(my_dict[key], list)):
        print(f"{key}:")
        for item in my_dict[key]:
            print(" -",item)
    else:
        print(key," : ",my_dict[key])
    
my_dict.pop("age") #remove based on key if key not availbale it will throw an error
print(my_dict)

my_dict.popitem() #removes last pair
print(my_dict)
