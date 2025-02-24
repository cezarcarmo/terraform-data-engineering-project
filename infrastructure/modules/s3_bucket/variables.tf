# Nome do bucket S3
variable "bucket_name" {
  description = "Nome do bucket S3"
  type        = string
}

# Controle de versionamento do bucket S3
variable "enable_versioning" {
  description = "Habilitar versionamento?"
  type        = bool
  default     = true
}
