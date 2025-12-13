provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "server1" {
  ami = var.ami_id
  instance_type = var.instance_type
  key_name = var.key_name
  vpc_security_group_ids = [aws_security_group.web_sg.id]
  tags = {
    Name: var.name_instance
  }
  user_data = <<-EOF
  #!/bin/bash
  apt update
  apt install -y nginx
  systemctl enable nginx
  systemctl start nginx
  EOF
}

resource "aws_security_group" "web_sg" {
  name = "web_sg"
  description = "Allow HTTP ans SSH"
  #inbound rule
  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  # outbound rule
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
