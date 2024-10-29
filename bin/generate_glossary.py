import os
import re

# Caminhos do repositório usando o diretório do script atual como referência
base_dir: str = os.path.dirname(os.path.abspath(__file__))  # Diretório do script
docs_dir: str = os.path.join(base_dir, "../docs")  # Caminho absoluto para a pasta docs
readme_path: str = os.path.join(base_dir, "../README.md")  # Caminho absoluto para o README.md

# Delimitadores da seção de glossário no README
start_marker = "<!-- início glossário -->"
end_marker = "<!-- término glossário -->"

def get_markdown_title_and_content(file_path: str) -> tuple[str | None, str]:
    print(f'Getting markdown title and content from {file_path}...')
    title: str | None = None
    content_lines: list = []
    first_title_found: bool = False  # Flag para verificar se o primeiro título foi encontrado

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("# "):
                title = line[2:].strip()  # Remove o '# ' e os espaços em branco # DOUBT: Need more details
                if not first_title_found:
                    content_lines.append(f"# {title}")  # O primeiro título é de nível 1
                    first_title_found = True
                else:
                    content_lines.append(f"## {title}")  # Títulos subsequentes são de nível 2
            else:
                content_lines.append(line.strip())

    if title is None:
        print(f'Warning: Title not found in {file_path}. Skipping file.')
    return title, "\n".join(content_lines)

def increment_title_levels(content: str) -> str:
    print("Original content before title level increment:\n", content)  # Log do conteúdo original

    # Aumenta o nível de título em 1 (de # para ##, de ## para ###, etc.)
    def replace_title(match):
        # DOUBT: Need more details
        level = match.group(1)  # Captura o nível de título
        title = match.group(2)   # Captura o título
        print(f"Found title: '{title}' with level '{level}'")  # Log do título encontrado
        
        # Incrementa o nível do título apenas se não exceder 6
        if len(level) < 6:  # Somente incrementa se não estiver no nível máximo
            new_level = '#' * (len(level) + 1)  # Aumenta o nível
            print(f"Incrementing title level from '{level}' to '{new_level}'")  # Log de incremento
            return f"{new_level} {title}"

        # Se for nível 6, ele se torna um tópico destacado por negrito apenas.
        if len(level) >= 6:
            return f"**{title}**"
        
        print(f"Title '{title}' is already at the maximum level.")  # Log se já estiver no nível máximo
        return match.group(0)  # Retorna a linha original se já estiver no nível máximo

    # Expressão regular para capturar títulos de níveis 1 a 5
    updated_content: str = re.sub(r'^(#+)\s+(.*)', replace_title, content, flags=re.MULTILINE) # DOUBT: Need more details
    print("Updated content after title level increment:\n", updated_content)  # Log do conteúdo atualizado

    return updated_content

def generate_glossary_content() -> str:
    print('Getting the docs list...')
    files: list[str] = [f.strip() for f in os.listdir(docs_dir) if f.lower().endswith(".md")]
    glossary_entries: list = []
    print("Files found:", files)

    for file_name in files:
        file_path: str = os.path.join(docs_dir, file_name)
        title, content = get_markdown_title_and_content(file_path)
        
        if title:
            print(f'Adding content for {title}...')
            # Aumenta os níveis de título no conteúdo
            content: str = increment_title_levels(content)
            glossary_entries.append(f"---\n{content}")

    print('Sorting the articles list...')
    glossary_entries.sort()
    glossary_content = "\n\n".join(glossary_entries) # DOUBT: Need more details
    print("Generated glossary content:\n", glossary_content)

    return glossary_content

def update_readme_with_glossary() -> None:
    glossary_content: str = generate_glossary_content()

    print('Getting the readme.md file...')
    with open(readme_path, "r", encoding="utf-8") as readme_file:
        readme_content: str = readme_file.read()

    if start_marker in readme_content and end_marker in readme_content:
        print("Markers found in README.md. Updating glossary section...")
        # DOUBT: Need more details
        new_content: str = re.sub(
            rf"{re.escape(start_marker)}.*?{re.escape(end_marker)}",
            f"{start_marker}\n\n{glossary_content}\n\n{end_marker}",
            readme_content,
            flags=re.DOTALL
        )
    else:
        print("Warning: Markers not found in README.md. Appending glossary section...")
        new_content = f"{readme_content}\n\n{start_marker}\n\n{glossary_content}\n\n{end_marker}"

    print('Saving the updated README.md...')
    with open(readme_path, "w", encoding="utf-8") as readme_file:
        readme_file.write(new_content)
    print("README updated with glossary content!")

if __name__ == "__main__":
    update_readme_with_glossary()
