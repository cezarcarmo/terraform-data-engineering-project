# Retorna o nome do bucket S3 criado
output "bucket_name" {
  description = "Nome do bucket S3 criado"
  value       = aws_s3_bucket.this.bucket
}
