provider "aws" {
  region = "us-east-1"
}

module "sg" {
  source = "./modules/security-group"
}

module "ec2" {
  source = "./modules/ec2"
  instance_name = "webserver1"
  sg = module.sg.security_group_id
}