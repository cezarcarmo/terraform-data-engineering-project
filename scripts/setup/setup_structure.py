import os
import shutil

# Definir novas pastas para organização
folders = [
    "infrastructure",
    "infrastructure/modules",
    "scripts/setup",
    "docs",
    "downloads",
    "environments/dev"
]

# Criar as pastas, se não existirem
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Função para mover arquivos apenas se ainda não existirem no destino
def safe_move(file, destination):
    dest_path = os.path.join(destination, os.path.basename(file))
    if os.path.exists(dest_path):
        print(f"⚠ Arquivo '{file}' já existe em '{destination}', pulando...")
    elif os.path.exists(file):
        shutil.move(file, destination)
        print(f"✅ Movido: {file} -> {destination}")

# Mover arquivos Terraform para a pasta infrastructure
terraform_files = ["main.tf", "outputs.tf", "variables.tf", "versions.tf"]
for file in terraform_files:
    safe_move(file, "infrastructure")

# Mover scripts para a pasta scripts/setup
safe_move("scripts/estrutura_principal.py", "scripts/setup")

# Mover arquivos de documentação para a pasta docs
docs_files = ["docs/setup_terraform.md", "docs/setup_tflint.md"]
for file in docs_files:
    safe_move(file, "docs")

# Mover arquivos zip para downloads
zip_files = ["terraform_1.10.5_windows_amd64.zip", "terraform_project.zip", "tflint_windows_amd64.zip"]
for file in zip_files:
    safe_move(file, "downloads")

# Criar um .gitignore aprimorado
gitignore_content = """# Terraform state files
.terraform/
terraform.tfstate
terraform.tfstate.backup

# Arquivos de log e cache
*.log
.cache/
__pycache__/

# Arquivos temporários
*.zip
*.bak
*.tmp
"""

gitignore_path = ".gitignore"
if not os.path.exists(gitignore_path):
    with open(gitignore_path, "w") as f:
        f.write(gitignore_content)
    print("✅ Criado: .gitignore")
else:
    print("⚠ O arquivo .gitignore já existe, pulando criação.")

print("\n🎯 Estrutura do projeto organizada com sucesso!")
