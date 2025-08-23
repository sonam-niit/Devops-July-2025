#!/bin/bash
for i in 1 2 3 4 5
do
    echo "Number: $i"
done

echo "Another way to iterate using range"
for i in {1..5}
do  
    echo "iteration: $i"
done
##While Loop
count=1
while [ $count -le 5 ]
do
    echo "Count: $count"
    ((count++))
done
##Untill Loop 
num=1
until [ $num -gt 5 ]
do
    echo "Num: $num"
    ((num++))
done
## Loops Through Files all txt files in current folder
for file in *.txt
do
    echo "Processing $file"
done