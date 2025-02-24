# Terraform Data Engineering Project

## 📌 Descrição

Este repositório demonstra o uso do Terraform para provisionar infraestrutura de Engenharia de Dados na AWS.

## 📂 Estrutura do Projeto

```
terraform-data-engineering-project/
├── infrastructure/
│   ├── main.tf
│   ├── outputs.tf
│   ├── variables.tf
│   ├── versions.tf
│   ├── modules/
│   │   └── s3_bucket/  (ainda precisa ser criado)
├── scripts/
│   ├── setup/
│   │   ├── estrutura_principal.py
├── docs/
│   ├── setup_terraform.md
│   ├── setup_tflint.md
├── environments/
│   ├── dev/
│   │   ├── backend.tf (se aplicável)
│   │   ├── terraform.tfvars
├── downloads/
│   ├── terraform_1.10.5_windows_amd64.zip
│   ├── terraform_project.zip
│   ├── tflint_windows_amd64.zip
├── .gitignore
├── LICENSE
├── README.md
```
