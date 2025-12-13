variable "aws_region" {
  description = "Aws Region"
  default = "us-east-1"
}
variable "ami_id" {
  description = "AMI Id for Server"
  type = string
}
variable "instance_type" {
  description = "EC2 instance Type"
  default = "t2.micro"
}
variable "key_name" {
  description = "EC2 Key Pair Name"
  type = string
}
variable "name_instance" {
  description = "name of the Instance"
  default = "WebServer"
}