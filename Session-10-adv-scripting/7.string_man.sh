#!/bin/bash
text="Hello World from Bash"

#Length of String
echo "Length: ${#text}"

echo "SubString: ${text:6:5}"

echo "Replace: ${text/World/Linux}" 

echo "Lowercase: ${text,,}"
echo "UpperCase: ${text^^}"

echo "Remove Prefix: ${text#* }"
echo "Remove Suffix: ${text% *}"