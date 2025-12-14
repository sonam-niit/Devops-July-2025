terraform {
  backend "s3" {
    bucket = "sonamsoni-basket"
    key="terraform.tfstate"
    region = "us-east-1"
  }
}

# after adding this file
# terraform init
# say yes 
# so now remote backend is configured successfully

# make sure you have sonamsoni-basket bucket exist in S3