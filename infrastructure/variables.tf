# Define a região da AWS
variable "aws_region" {
  description = "Região da AWS para provisionar os recursos"
  type        = string
  default     = "us-east-1"
}

# Nome do bucket S3
variable "bucket_name" {
  description = "Nome do bucket S3"
  type        = string
  default     = "meu-bucket-data-engineering"
}

# Controle de versionamento do bucket S3
variable "enable_versioning" {
  description = "Habilitar versionamento no S3?"
  type        = bool
  default     = true
}
