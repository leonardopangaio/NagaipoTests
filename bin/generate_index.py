import os
import re

# Caminhos do repositório usando o diretório do script atual como referência
base_dir: str = os.path.dirname(os.path.abspath(__file__))  # Diretório do script
docs_dir: str = os.path.join(base_dir, "../docs")  # Caminho absoluto para a pasta docs
readme_path: str = os.path.join(base_dir, "../README.md")  # Caminho absoluto para o README.md


def get_markdown_title(file_path: str) -> str | None:
    print(f'Getting markdown title from {file_path}...')
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("# "):
                return line[2:].strip()  # Remove o '# ' e os espaços em branco
    return None

def generate_index() -> None:
    print('Getting the docs list...')
    # Obter todos os arquivos .md na pasta docs
    files: list[str] = [f.strip() for f in os.listdir(docs_dir) if f.lower().endswith(".md")]
    index_entries: list[str] = []
    print("Files found:", files)

    for file_name in files:
        file_path: str = os.path.join(docs_dir, file_name)
        title: str | None = get_markdown_title(file_path)
        
        if title:
            print(f'Creating link for {title}...')
            link: str = f"[{title}](docs/{file_name})"
            index_entries.append(link)

    # Ordenar o índice em ordem alfabética
    print('Sorting the index list...')
    index_entries.sort()
    print("Index entries:", index_entries)

    # Criar o conteúdo do índice como título secundário
    print('Creating index content...')
    index_content: str = "## Índice\n\n" + "\n".join(f"- {entry}" for entry in index_entries)
    print("Generated index content:\n", index_content)

    # Ler o conteúdo atual do README.md
    print('Getting the readme.md file...')
    with open(readme_path, "r", encoding="utf-8") as readme_file:
        readme_content: str = readme_file.read()

    # Se já houver um índice, substituí-lo; caso contrário, adicionar no final
    print('Writing the new content on readme.md...')
    if "## Índice" in readme_content:
        # Substituir o índice existente
        new_content: str = re.sub(r"(?s)(## Índice\n\n.*?)(?=#|\Z)", index_content, readme_content)
    else:
        # Adicionar o índice no final
        new_content: str = readme_content.strip() + "\n\n" + index_content

    # Escrever o conteúdo atualizado no README.md
    print('Saving the new readme.md file...')
    with open(readme_path, "w", encoding="utf-8") as readme_file:
        readme_file.write(new_content)

if __name__ == "__main__":
    generate_index()
    print("Index updated!")
