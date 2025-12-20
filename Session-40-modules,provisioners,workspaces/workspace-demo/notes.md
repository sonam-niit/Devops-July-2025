# how to create workspace

```bash
terraform init
terraform workspace new dev
terraform workspace new prod
terraform workspace list # see all workspaces
terraform workspace show # see current workspace
terraform workspace select dev # now it will use dev workspace
terraform apply --auto-approve
# create dev instance
terraform workspace select prod
terraform apply --auto-approve
# create prod instance
```
- if you check state folder (state maintaained seperately)
- terraform.tfstate.d/
- dev/
    - terrafor.tfstate
- prod/
    - terrafor.tfstate

# pass variables directly from variables.tf file
- use default as shown here
# pass using tfvars file

- create variable as string
- create folder tfvars
- under that create 2 files dev.tfvars & prod.tfvars
- this files not loaded automatically so we need to passas argument

```bash
terraform workspace select dev
terraform apply -var-file=tfvars/dev.tfvars --auto-approve
```

# another way to use locals

- create locals.tf file
- use values in main.tf directly from local based on workspace