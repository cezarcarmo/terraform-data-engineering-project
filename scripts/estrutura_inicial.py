import os

# Definir a lista de arquivos principais a serem criados
files = {
    "README.md": "# Terraform Data Engineering Project\n\nEste repositório contém um exemplo prático de uso do Terraform na Engenharia de Dados.",
    
    "versions.tf": """terraform {
  required_version = ">= 1.0.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}""",

    "variables.tf": """variable "aws_region" {
  description = "Região da AWS para provisionar os recursos"
  type        = string
  default     = "us-east-1"
}""",

    "outputs.tf": """output "example_output" {
  description = "Exemplo de output do Terraform"
  value       = "Terraform configurado corretamente"
}""",

    "main.tf": """# Arquivo principal do Terraform

module "example" {
  source = "./modules/example_module"
}"""
}

# Criar os arquivos diretamente na pasta atual
for file_name, content in files.items():
    with open(file_name, "w") as f:
        f.write(content)

# Exibir os arquivos criados
os.listdir(os.getcwd())
