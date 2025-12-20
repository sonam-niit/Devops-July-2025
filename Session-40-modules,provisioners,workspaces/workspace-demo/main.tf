provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  ami = "ami-020cba7c55df1f615"
#   instance_type = var.instance_type
#   instance_type = lookup(var.instance_type, terraform.workspace)
    instance_type = local.config[local.env].instance_type
    root_block_device {
      volume_size = local.config[local.env].volume_size
    }
#   count = 2
  tags = {
    # Name = "myapp-${terraform.workspace}"
    Name = "myapp-${local.env}"
  }
}