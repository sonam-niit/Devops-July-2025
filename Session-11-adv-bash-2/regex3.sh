#!/bin/bash

read -rp "Enter your IP address: " ip
# Step 1: Validate IP format
if [[ ! $ip =~ ^([0-9]{1,3}\.){3}[0-9]{1,3}$ ]]; then
    echo "Invalid IP format"
    exit 1
fi
# Step 2: Validate each octet range (0–255)
IFS='.' read -r o1 o2 o3 o4 <<< "$ip"
for octet in $o1 $o2 $o3 $o4; do
    if (( octet < 0 || octet > 255 )); then
        echo "Invalid IP address (octet out of range)"
        exit 1
    fi
done

echo "Valid IP address"
