#Array Declaration
names=("alex" "john" "catty" "bob" "devid")

#Access Elements
echo "First Element: ${names[0]}"
echo "Third Element: ${names[2]}"

# Access Length
echo "Total Names: ${#names[@]}"
echo "All Names: ${names[@]}"

#Change Array Element
names[1]="John Doe"
echo "Updated Element: ${names[1]}"

#Print ALL
for name in "${names[@]}";do 
    echo "$name"
done

#Print them in one line
result=""
for name in "${names[@]}";do 
    result+="$name ,"
done

echo "${result%,}" #remove last ,