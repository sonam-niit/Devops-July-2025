output "bucket_name" {
  description = "Name of the Bucket"
  value= aws_s3_bucket.website_bucket.bucket
}

output "bucket_arn" {
  description = "Bucket ARN"
  value = aws_s3_bucket.website_bucket.arn
}

output "website_endpoint" {
  description = "Website Endpoint"
  value = aws_s3_bucket_website_configuration.website_config.website_endpoint
}