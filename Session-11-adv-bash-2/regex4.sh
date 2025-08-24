read -rp "Enter any text: " email
if [[ $email =~ ^ab*c$ ]]; then
    echo "Valid Text"
else
    echo "Invalid Text"
fi

# Correct patterns
# ac
# abc
# abbbbc
# Incorrect
# abba #aabbc #abbbac