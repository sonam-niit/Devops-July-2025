#!/bin/bash
read -rp "Enter Your IP: " ip
if [[ $ip =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]
then
  echo "Valid IP"
else
  echo "Invalid IP"
fi

#!/bin/bash

read -p "Enter an IP address: " ip
ip="^([0-9]{1,3}\.){3}[0-9]{1,3}$"

if [[ $ip =~ $ip ]]; then
        echo "connect"
    else
        echo "Disconnect"
    fi

