# Exibe o nome do bucket S3 criado
output "s3_bucket_name" {
  description = "Nome do bucket S3 criado"
  value       = module.s3_bucket.bucket_name
}
