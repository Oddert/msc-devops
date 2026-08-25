provider "aws" {
    region = "eu-west-2"
}

terraform {
    backend "s3" {
    }
}

variable "env_prefix" { }
variable "is_temp_env" {
    default = false
}

resource "aws_s3_bucket" "b" {
    bucket = "${var.env_prefix}do-demo.com"
    force_destroy = var.is_temp_env

    website {
      index_document = "index.html"
    }

    tags = {
      ManagedBy = "terraform"
    }
}

resource "aws_s3_bucket_policy" "b_policy" {
    bucket = aws_s3_bucket.b.id

    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Sid       = "PublicReadGetObject"
          Effect    = "Allow"
          Principal = "*"
          Action    = "s3:GetObject"
          Resource  = "${aws_s3_bucket.b.arn}/*"
        }
      ]
    })
}

resource "aws_s3_bucket_acl" "b_acl" {
    bucket = aws_s3_bucket.b.id
    acl    = "public-read"
}

output "website" {
    value = "http://${aws_s3_bucket.b.website_endpoint}"
}
