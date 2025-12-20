locals {
  env= terraform.workspace

  config = {
    dev = {
        instance_type="t2.micro"
        volume_size=8
    }

    prod = {
        instance_type="t3.micro"
        volume_size=20
    }
  }
}