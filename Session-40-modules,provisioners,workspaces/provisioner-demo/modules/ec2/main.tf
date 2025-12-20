resource "aws_instance" "web" {
  ami = var.ami
  instance_type = var.instance_type
  key_name = "ansiblekey"
  vpc_security_group_ids = [var.sg]
  tags = {
    Name= var.instance_name
  }

  connection {
    type = "ssh"
    user = "ubuntu"
    private_key = file("~/.ssh/ansiblekey.pem")
    host = self.public_ip
  }

  provisioner "remote-exec" {
    inline = [ 
      "sudo apt update",
      "sudo apt install -y nginx",
      "sudo systemctl start nginx"
     ]
  }
}