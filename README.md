# AI Sticky Notes

Um aplicativo simples de notas rápidas ("sticky notes") com interface web e integração com AI, desenvolvido em Python usando Flask e MCP.

## Funcionalidades

- Adicione notas rápidas via interface web ou linha de comando.
- Visualize todas as notas salvas.
- Veja a nota mais recente.
- Gere um prompt para resumo das notas (útil para integração com IA).
- Persistência das notas em arquivo local (`notes.txt`).

## Requisitos

- Python 3.8+
- [Flask](https://flask.palletsprojects.com/)
- MCP (FastMCP) - biblioteca customizada (presumida no projeto)

## Instalação

1. Clone este repositório ou copie os arquivos para uma pasta local.
2. Instale as dependências:
   ```bash
   pip install flask
   ```
   (Adicione outras dependências se necessário.)

## Como usar

### Modo Web

Execute o servidor web:
```bash
python web.py
```
Acesse em [http://localhost:5000](http://localhost:5000) no navegador.

### Modo Linha de Comando

Execute:
```bash
python main.py
```
Siga as instruções no terminal para adicionar, visualizar ou resumir notas.

### Modo Servidor MCP

Para rodar como serviço MCP:
```bash
python main.py --serve
```

## Estrutura dos Arquivos

- `main.py`: Lógica principal das notas e integração MCP.
- `web.py`: Interface web com Flask.
- `notes.txt`: Arquivo local onde as notas são salvas.
- `README.md`: Este arquivo.

## Observações

- O projeto utiliza um arquivo de texto simples para armazenar as notas.
- O prompt de resumo pode ser usado para integração com modelos de IA para gerar resumos automáticos.

## Licença

MIT (ou especifique a licença do seu projeto)

---
Desenvolvido para fins de demonstração.
