#!/bin/bash
# If statement
num=10
if [ $num -gt 5 ]
then 
    echo "Numbet is greater than 5"
fi
#If else statement
name="Test"
if [ $name = "Sonam" ]
then
    echo "Hello Sonam!"
else
    echo "Hello guest!"
fi
#Logical Operators
age=45
if [ $age -ge 18 ] && [ $age -lt 60 ]
then    
    echo "Eligible adult"
fi
user="root"
if [ $user = "admin" ] || [ $user = "root" ]
then    
    echo "You have an admin access"
fi