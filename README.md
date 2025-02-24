# 🚀 Projeto Terraform para Engenharia de Dados

Este repositório demonstra como utilizar o **Terraform** para provisionar infraestrutura na **AWS**, aplicada à **Engenharia de Dados**. O projeto é modular e permite a criação de um **bucket S3** para armazenar dados, seguindo as **melhores práticas de infraestrutura como código (IaC)**.

---

## 📌 **Objetivos do Projeto**

✅ Provisionar um **bucket S3** na AWS utilizando Terraform.  
✅ Aplicar **boas práticas de modularização** no Terraform.  
✅ Configurar o **AWS CLI** para gerenciar recursos de forma segura.  
✅ Criar um **módulo reutilizável** para facilitar a criação de múltiplos buckets.  
✅ Demonstrar a **importância do Terraform** para Engenharia de Dados.  

---

## 📂 **Estrutura do Repositório**

```
terraform-data-engineering-project/
├── infrastructure/               # Infraestrutura Terraform
│   ├── main.tf                   # Chama o módulo e provisiona o bucket S3
│   ├── outputs.tf                # Outputs do Terraform
│   ├── variables.tf              # Variáveis globais
│   ├── versions.tf               # Configuração do provider AWS
│   ├── modules/                   # Módulos reutilizáveis
│   │   ├── s3_bucket/              # Módulo para criação do bucket S3
│   │   │   ├── main.tf             # Código principal do módulo
│   │   │   ├── outputs.tf          # Outputs do módulo
│   │   │   ├── variables.tf        # Variáveis do módulo
├── scripts/                       # Scripts auxiliares
│   ├── setup/                     # Scripts de configuração
│   │   ├── estrutura_principal.py  # Script de automação inicial
├── docs/                           # Documentação
│   ├── setup_terraform.md          # Guia de instalação do Terraform
│   ├── setup_tflint.md             # Guia de instalação do TFLint
│   ├── setup_aws.md                # Guia de configuração da AWS
├── environments/                    # Configuração de ambientes
│   ├── dev/                         # Ambiente de desenvolvimento
│   │   ├── backend.tf (se aplicável)
│   │   ├── terraform.tfvars         # Variáveis específicas do ambiente dev
├── downloads/                        # Arquivos baixados
│   ├── terraform_1.10.5_windows_amd64.zip
│   ├── terraform_project.zip
│   ├── tflint_windows_amd64.zip
├── .gitignore                        # Arquivos ignorados pelo Git
├── LICENSE                           # Licença do projeto
├── README.md                         # Documentação principal

```

---

# 🛠 **1. Configuração da Conta AWS**

Para que o Terraform possa gerenciar seus recursos, siga os passos abaixo:

### **1️⃣ Criar um Usuário IAM na AWS**

1. Acesse o serviço **IAM**:  
   🔗 [https://console.aws.amazon.com/iam](https://console.aws.amazon.com/iam)
2. Vá em **Usuários** → **Adicionar Usuário**.
3. Defina um nome: `terraform-user`
4. Marque **Acesso Programático**.
5. Em **Permissões**, selecione:
   - `AdministratorAccess` _(para testes)_  
   - Ou `AmazonS3FullAccess` _(se for usar apenas S3)_
6. Gere e **anote suas credenciais** (Access Key e Secret Key).

### **2️⃣ Instalar e Configurar o AWS CLI**

Baixe e instale o AWS CLI:

```sh
aws configure
```

Digite suas credenciais da AWS:

```
AWS Access Key ID [None]: AKIAXXXXXXXXXXXXXXXX
AWS Secret Access Key [None]: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Default region name [None]: us-east-1
Default output format [None]: json
```

Para testar a conexão com a AWS:

```sh
aws s3 ls
```

---

# 🚀 **2. Como Usar Este Projeto**

### **1️⃣ Inicializar o Terraform**

```sh
terraform init
```

### **2️⃣ Validar a Configuração**

```sh
terraform validate
```

### **3️⃣ Visualizar as Alterações**

```sh
terraform plan
```

### **4️⃣ Aplicar as Mudanças (Criar Infraestrutura)**

```sh
terraform apply
```

Digite `yes` quando solicitado.

### **5️⃣ Verificar se o Bucket foi Criado**

```sh
aws s3 ls
```

### **6️⃣ Para Destruir a Infraestrutura**

```sh
terraform destroy
```

Isso **excluirá todos os recursos** criados pelo Terraform.

---

## 📌 **3. Expansão do Projeto**

### 🔹 **O que mais pode ser adicionado?**

✔ Criar um **Glue Data Catalog** para organizar os dados.  
✔ Criar um **Redshift Cluster** para armazenar grandes volumes de dados.  
✔ Configurar **Remote State** no S3 para projetos colaborativos.  
✔ Automatizar deploys com **GitHub Actions**.  

---

## 📖 **4. Documentação Adicional**

📂 **Guia de Configuração da AWS:** [`setup_aws.md`](docs/setup_aws.md)  
📂 **Documentação Oficial do Terraform:** [terraform.io/docs](https://developer.hashicorp.com/terraform/docs)  

---

## 🎯 **5. Conclusão**

Agora você tem um **projeto funcional e modular** para provisionar infraestrutura na AWS com Terraform! 🚀  

✅ Infraestrutura como Código (**IaC**) aplicada à **Engenharia de Dados**.  
✅ **Provisionamento automatizado** de recursos na AWS.  
✅ **Código modular** e reutilizável para diferentes cenários.  

⚡ **Gostou do projeto?** Dê um ⭐ no GitHub e contribua! 😃
