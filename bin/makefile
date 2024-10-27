# Versão do Makefile
VERSION="2.4.0"
SHELL := /bin/bash

# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help: ## Mostra essa ajuda/descrição
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

version: ## Mostra a versão do arquivo makefile
	@echo "A versão do Makefile é: $(VERSION)"

venv: ## Criação de ambiente virtual para Python
	@python3 -m venv venv

install_lib: venv requirements.txt ## Instalação das dependências
	@source venv/bin/activate \
		&& pip3 install --upgrade pip \
		&& pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt

run_python: venv ## Testa execução do script Python
	@source venv/bin/activate && python3 main.py

requirements.txt: venv ## Gera o arquivo requirements.txt com as dependências
	@if [ ! -f requirements.txt ]; then \
			source venv/bin/activate \
			&& pip3 install pipreqs \
			&& pipreqs .; \
	fi

fix_reqs: venv ## Gera o requirements.txt baseado no que está instalado no venv
	@source venv/bin/activate \
		&& pip3 freeze > requirements.txt 

git: ## Realiza o update do repositório
	@git fetch origin \
		&& git pull --no-rebase
