#!/bin/bash

read -rp "Enter Something: " data
test=($data =~ ^[0-9]+$)
if [ $test ]; then
# if [[ $data =~ ^[0-9]+$ ]]; then ##use 4-5 line or only 6
    # echo "It's an integer number"
    echo "It's an integer number"
else
    echo "Not an integer number"
fi

# -r prevents backslash(\) interpreted as escape char
# -p printes and read input in variable named data

# =~ : Regex match operator in Bash
## [[ ... ]] Advanced Bash Test command
## more powerful than [ ... ]