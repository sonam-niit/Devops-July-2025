# ASG

- run below commands

```bash
terraform init 
terraform apply --auto-approve
# by default it will create only one instance

# connect with instace from browser only
# increase load

yes > /dev/null &

# check load by using top command
# if it cross no of instance will increase

```

- go to asg (auto scaling group in aws console)
- activity -> check history

- there you can see instance added from 0-1 and 1-2 like that

```bash
# stop load
killall yes
# again check activity
# make sure to destroy all resources
terraform destroy --auto-approve
```