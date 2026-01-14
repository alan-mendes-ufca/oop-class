# Projeto de revisão POO

## Poetry

- É um gerenciador de pacotes alternativo ao pip, bem semelhante ao npm.
- Para inicializar o projeto python basta fazer `poetry init` ou `poetry new <...>`
- Para instalar dependências: `poetry add <...>`
- Também é possível executar scripts: `poetry run python your_script.py` e outras ferramentas de comando como `poetry run python pytest`

## Executando

`poetry run mini-library`
ou para executar o pytest
`poetry run pytest`

## Rotinas

- Muda pyproject.toml → rode `poetry install`
- Adiciona dependência → rode `poetry lock` depois `poetry install`
