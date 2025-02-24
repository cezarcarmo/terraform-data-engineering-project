# Criar o bucket S3
resource "aws_s3_bucket" "this" {
  bucket = var.bucket_name
}

# Configuração de versionamento do bucket S3
resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.this.id
  versioning_configuration {
    status = var.enable_versioning ? "Enabled" : "Suspended"
  }
}
