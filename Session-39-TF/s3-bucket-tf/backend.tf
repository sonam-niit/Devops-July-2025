terraform {
  backend "s3" {
    bucket = "sonamsoni-basket"
    key="terraform.tfstate"
    region = "us-east-1"
    encrypt = true # to enable server side encryption
    # because state file includes credentials and some secret info
    dynamodb_table = "name-of-table-created-on-aws" #used for state locking
  }
}

# after adding this file
# terraform init
# say yes 
# so now remote backend is configured successfully

# make sure you have sonamsoni-basket bucket exist in S3