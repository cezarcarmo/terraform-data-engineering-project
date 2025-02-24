# Chama o módulo s3_bucket para criar um bucket S3
module "s3_bucket" {
  source             = "./modules/s3_bucket"
  bucket_name        = var.bucket_name
  enable_versioning  = var.enable_versioning
}
