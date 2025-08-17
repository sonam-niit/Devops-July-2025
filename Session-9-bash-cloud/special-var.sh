#!/bin/bash
echo "Script Name: $0"
echo "Total No of arguments: $#"
echo "First argument: $1"
echo "Second argument: $2"
echo "All arguments: $@"
echo "Process Id: $$"
echo "Exit Status: $?"

# Run above script using below command
# sh special-var.sh 67 sonam true hello xyz
# here (67 sonam true hello xyz) are the arguments  

#./special-var.sh file1.txt file2.txt
# here 1st arg: file1.txt
# here 2nd arg: file2.txt