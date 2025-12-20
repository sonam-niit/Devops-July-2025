provider "aws" {
  region = "us-east-1"
}
module "vpc" {
  source = "./modules/vpc"
  cidr_block = "10.0.0.0/16"
  subnet_cidr = "10.0.1.0/24"
  availability_zone = "us-east-1a"
}

module "security_group" {
  source = "./modules/security-group"
  vpc_id = module.vpc.vpc_id
}

module "ec2" {
  source = "./modules/ec2"
  subnet_id = module.vpc.subnet_id
  security_group_id = module.security_group.security_group_id
  instance_name = "webserver1"
}