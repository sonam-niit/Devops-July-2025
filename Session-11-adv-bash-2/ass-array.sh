declare -A capitals
capitals[India]="New Delhi"
capitals[France]="Paris"
capitals[Japan]="Tokyo"

##Access
echo "Capital of Japan is ${capitals[Japan]}"
## iterate with values
for capital in "${capitals[@]}"; do
    echo "$capital"
done

## iterate with key and value both
# ! expands keys
for country in "${!capitals[@]}"; do
    echo "Capital of $country is ${capitals[$country]}"
done