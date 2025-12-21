# Launch template
resource "aws_launch_template" "demo_lt" {
  name_prefix   = "demo_lt"
  image_id      = "ami-08a6efd148b1f7504" #Amazon Linux
  instance_type = "t2.micro"
  vpc_security_group_ids = [ aws_security_group.asg_sg.id ]
  user_data = base64encode(<<EOF
#!/bin/bash
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "Hello From Auto Scaling Group" >/var/www/html/index.html
EOF  
)
}

# Auto Scaling group
resource "aws_autoscaling_group" "demo_asg" {
  name = "demo_asg"
  min_size = 1
  max_size = 2
  desired_capacity = 1

  tag {
    key = "Name"
    value = "asg-demo-instance"
    propagate_at_launch = true
  }
  launch_template {
    id = aws_launch_template.demo_lt.id
    version = "$Latest"
  }
}

# Security Group
resource "aws_security_group" "asg_sg" {
  name = "asg_sg"
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

resource "aws_autoscaling_policy" "cpu_scaling" {
  name = "cpu_target_scaling"
  policy_type = "TargetTrackingScaling"
  autoscaling_group_name = aws_autoscaling_group.demo_asg.name

  target_tracking_configuration {
    predefined_metric_specification {
      predefined_metric_type = "ASGAverageCPUUtilization"
    }
    target_value = 50.0
  }
}