# Define a versão mínima do Terraform e os provedores utilizados
terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0.0"
    }
  }
}

# Configuração do provedor AWS
provider "aws" {
  region = var.aws_region
}
