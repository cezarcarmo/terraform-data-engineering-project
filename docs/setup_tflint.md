# Configuração do TFLint no Windows

Este guia descreve como baixar, instalar e configurar o TFLint no Windows.

## O que é o TFLint?

TFLint é uma ferramenta de linting para Terraform que ajuda a encontrar possíveis problemas em seus arquivos de configuração do Terraform. Ele verifica a sintaxe, a conformidade com as melhores práticas e possíveis erros de configuração antes de você aplicar suas mudanças na infraestrutura. Isso ajuda a garantir que suas configurações estejam corretas e otimizadas, reduzindo a chance de erros durante a execução do Terraform.

## Passos para Instalação

1. **Baixe a última versão do TFLint:**
   ```sh
   curl -LO https://github.com/terraform-linters/tflint/releases/download/v0.44.1/tflint_windows_amd64.zip

2. **Extraia o arquivo zipado:**
   ```sh
   unzip tflint_windows_amd64.zip

3. Crie o diretório `tflint` se ele não existir e mova o binário extraído para o diretório:
   ```sh   
   mkdir -p /c/tflint/
   mv tflint.exe /c/tflint/

4. Adicione `tflint` ao PATH:
   ```sh
   export PATH=$PATH:/c/tflint

5. Feche e reabra o terminal para que as mudanças sejam aplicadas.

6. Verifique se o terminal está usando o binário correto do TFLint:
   ```sh
   tflint --version

