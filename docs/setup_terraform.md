## Configurando o Terraform no Windows

Para atualizar o Terraform no Windows, siga os passos abaixo:

1. Baixe a última versão do Terraform:
   ```sh
   curl -LO https://releases.hashicorp.com/terraform/1.10.5/terraform_1.10.5_windows_amd64.zip

2. Extraia o arquivo zipado:
   ```sh
   unzip terraform_1.10.5_windows_amd64.zip

3. Crie o diretório `terraform` se ele não existir:
   ```sh
   mkdir -p /c/terraform/
	
4. Mova o binário extraído para o diretório `terraform`:
   ```sh
   mv terraform.exe /c/terraform/

5. Adicione `terraform` ao PATH:

    * Abra o menu Iniciar e procure por "Variáveis de Ambiente".
    * Clique em "Editar as variáveis de ambiente do sistema".
    * Na janela "Propriedades do Sistema", clique em "Variáveis de Ambiente".
    * Na seção "Variáveis do sistema", encontre a variável Path e clique em "Editar".
    * Na janela "Editar variável de ambiente", clique em "Novo" e adicione terraform.
    * Salve as alterações e Clique em "OK" para fechar todas as janelas.

6. Feche e reabra o terminal para que as mudanças sejam aplicadas.
7. Verifique se o terminal está usando o binário correto do Terraform:
   ```sh
   terraform --version
	
8. Se o problema persistir, você pode adicionar temporariamente o diretório ao PATH para a sessão atual do terminal:
   ```sh
   export PATH=$PATH:/c/terraform

9. Depois disso, verifique novamente a versão do Terraform:
   ```sh
   terraform --version
	
 