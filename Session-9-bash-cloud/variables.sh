#!/bin/bash
my_name="Sonam Soni"
echo "My Name is $my_name"
echo "Enter Your Age"
read age # read user Input
echo "I am $age years old"

## Arithmetic Operations
a=10
b=20
sum=$((a+b)) ## $(()) for Math
echo "Sum = $sum"

#Samples
user="John Doe"
today=$(date +%Y/%m/%d-%H:%M:%S)

echo "Hello $user, today is $today"