read -rp "\"Enter an Email: \"" email
if [[ $email =~ ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$ ]]; then
    echo "Valid Email Addess"
else
    echo "Invalid Email Address"
fi

##### 5 min task #####
## Write a code to take IP from user
## Write reg exp to validate IP 
## If matches pattern print connected
## Else print incorrect IP

## Match Exactly 8 digits in a row with simple regex
# Pattern [0-9]{8}

