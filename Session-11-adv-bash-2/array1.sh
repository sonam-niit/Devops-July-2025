#Array Operations
nums=(1 2 3 4 5)
echo "${nums[@]}"
#Append
nums+=(6)
echo "After Append ${nums[@]}"
#Append Multiple
nums+=(7 8 9 10)
echo "After Append ${nums[@]}"
#Insert at specific Index
nums[3]=20
echo "After insert ${nums[@]}" #Replace
nums[11]=90
echo "After Append ${nums[@]}"
#delete
unset nums[3]
echo "After Append ${nums[@]}"
#insert 4 between 3 and 5
index=3
nums=("${nums[@]:0:$index}" 4 "${nums[@]:$index}")
echo "After Insert in between ${nums[@]}"