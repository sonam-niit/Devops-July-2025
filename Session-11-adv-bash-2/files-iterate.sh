# iterate output of some command
for file in $(ls *.*); do
    echo $file
done


# Iterate lines of file
for line in $(cat array.sh); do
    echo $line
done