variable "ami" {
  description = "Image Id"
  default = "ami-020cba7c55df1f615"
}

variable "instance_type" {
  description = "Instance type"
  default = "t2.micro"
}
variable "instance_name" {
  description = "Name of the instance"
}
variable "sg" {
  description = "Security Group"
}