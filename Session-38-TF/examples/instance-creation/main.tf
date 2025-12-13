provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "server1" {
  ami = "ami-020cba7c55df1f615"
  instance_type = "t2.micro"
  key_name = "ansiblekey"
  tags = {
    Name: "sonamvm"
  }
}

# terraform init
# terraform apply --auto-approve
# terraform destroy --auto-approve