# Financiamentos — Web Server Python

Servidor Flask para hospedar as páginas HTML de financiamentos no Render.

## Estrutura de arquivos

```
/
├── app.py               ← servidor Flask
├── requirements.txt     ← dependências
├── render.yaml          ← config do Render
├── templates/           ← coloque aqui todos os HTMLs do repositório original
│   ├── index.html
│   ├── financiamento-carro-usado.html
│   ├── financiamento-moto-honda.html
│   ├── googlee9e345b2ea532dde.html
│   ├── juros-financiamento-2026.html
│   ├── simulador-sem-entrada.html
│   └── ads.txt.txt
└── static/              ← CSS, JS, imagens (se houver)
```

## Como fazer o deploy no Render

1. Copie todos os arquivos `.html` do repositório original para a pasta `templates/`
2. Se houver CSS/JS/imagens, coloque na pasta `static/`
3. Suba tudo para o GitHub
4. No Render, crie um novo **Web Service** apontando para o repositório
5. O `render.yaml` já configura tudo automaticamente

## Rotas disponíveis

| URL | Arquivo |
|-----|---------|
| `/` | index.html |
| `/financiamento-carro-usado` | financiamento-carro-usado.html |
| `/financiamento-moto-honda` | financiamento-moto-honda.html |
| `/juros-financiamento-2026` | juros-financiamento-2026.html |
| `/simulador-sem-entrada` | simulador-sem-entrada.html |
| `/googlee9e345b2ea532dde.html` | verificação Google |
| `/ads.txt` | ads.txt.txt |

## Rodar localmente

```bash
pip install -r requirements.txt
python app.py
# Acesse http://localhost:5000
```