provider "local" {}

resource "local_file" "sample" {
  filename = "hello.txt"
  content = "Hello From Terraform"
}

# open this folder in terminal
# run below commands
# terrform init: it will create .terrform folder and .terraform.lock.hcl file
# terraform plan: will the the plan for resource creation
# terraform apply (say yes manually) 
# will create resources and also create state files
# for auto yes use: terraform apply --auto-approve
# terraform destroy --auto-approve (to destroy the resources)

