name="Guest"
age=0

while getopts "n:a:h" opt; do
    case $opt in
        n) # -n <name>
            name=$OPTARG
            ;;
        a) # -a <age>
            age=$OPTARG
            ;;
        h) # -h <hello>
            echo "Usage: $0 [-n name] [-a age] [-h]"
            exit 0
            ;;
        \?) # Invalid Option
            echo "Invalid option: -$OPTARG"
            exit 1
            ;;
        esac
    done
#Print Values
echo "Name: $name"
echo "Age: $age"