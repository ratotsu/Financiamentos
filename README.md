# Financiamentos — Web Server Python

Servidor Flask para hospedar as páginas HTML de financiamentos.

## 📋 Estrutura de arquivos

```
/
├── app.py                           ← servidor Flask com segurança
├── requirements.txt                 ← dependências
├── render.yaml                      ← configuração de deploy
├── .env.example                     ← exemplo de variáveis de ambiente
├── .gitignore                       ← arquivos a ignorar no git
├── ads.txt                          ← arquivo para ads
├── templates/                       ← arquivos HTML
│   ├── index.html
│   ├── financiamento-carro-usado.html
│   ├── financiamento-moto-honda.html
│   ├── googlee9e345b2ea532dde.html
│   ├── juros-financiamento-2026.html
│   ├── simulador-sem-entrada.html
│   └── ads.txt
└── static/                          ← CSS, JS, imagens (se houver)
```

## 🚀 Rotas disponíveis

| URL | Arquivo |
|-----|---------|
| `/` | index.html |
| `/financiamento-carro-usado` | financiamento-carro-usado.html |
| `/financiamento-moto-honda` | financiamento-moto-honda.html |
| `/juros-financiamento-2026` | juros-financiamento-2026.html |
| `/simulador-sem-entrada` | simulador-sem-entrada.html |
| `/googlee9e345b2ea532dde.html` | Verificação Google |
| `/ads.txt` | ads.txt |
| `/static/*` | Arquivos estáticos (CSS, JS, imagens) |

## 💻 Rodar localmente

### Pré-requisitos
- Python 3.11+
- pip

### Instalação

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd Financiamentos
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. (Opcional) Configure variáveis de ambiente:
```bash
cp .env.example .env
# Edite .env com seus valores
```

5. Execute o servidor:
```bash
python app.py
```

6. Acesse em seu navegador:
```
http://localhost:5000
```

## 📦 Deploy no Render

### Passos

1. **Prepare o repositório:**
   - Todos os arquivos `.html` devem estar em `templates/`
   - Arquivos estáticos (CSS, JS, imagens) devem estar em `static/`
   - Arquivos `.py`, `requirements.txt` e `render.yaml` na raiz

2. **Configure no Render:**
   - Crie uma conta em https://render.com
   - Crie um novo **Web Service**
   - Conecte seu repositório GitHub
   - Deixe o `render.yaml` configurar automaticamente

3. **Variáveis de Ambiente (no Render):**
   - `FLASK_ENV` = `production`
   - `PYTHON_VERSION` = `3.11.0`
   - Adicione qualquer outra variável necessária do `.env.example`

### Resultado

Seu site estará disponível em:
```
https://<seu-app>.onrender.com
```

## 🔒 Segurança

A aplicação inclui:
- ✅ Headers de segurança HTTP (X-Frame-Options, Content-Type-Options, etc.)
- ✅ Cache control inteligente (estáticos com cache, páginas sem cache)
- ✅ Logging de requisições e erros
- ✅ Tratamento de erros 404 e 500
- ✅ Proteção contra cliques maliciosos (X-Frame-Options)

## 📊 Monitoramento

Os logs da aplicação incluem:
- Todas as requisições (DEBUG)
- Acessos a páginas (INFO)
- Avisos de arquivo não encontrado
- Erros do servidor (ERROR)

## 🛠️ Desenvolvimento

### Adicionar Nova Página

1. Crie o arquivo HTML em `templates/nomelimpo.html`
2. Adicione a rota em `app.py`:
```python
@app.route("/nomelimpo")
@app.route("/nomelimpo.html")
def nomelimpo():
    logger.info("Acesso à página de nomelimpo")
    return send_from_directory(TEMPLATES_DIR, "nomelimpo.html")
```

### Adicionar Estilos ou Scripts

1. Crie a pasta `static/` se não existir
2. Organize em subpastas: `static/css/`, `static/js/`, `static/images/`
3. Referencie em seus HTMLs:
```html
<link rel="stylesheet" href="/static/css/estilo.css">
<script src="/static/js/script.js"></script>
<img src="/static/images/logo.png" alt="Logo">
```

## 📝 Notas Importantes

- A aplicação roda com `debug=False` em produção
- Não use a porta 5000 em produção - use a definida pela variável `PORT`
- Sempre use HTTPS em produção (Render redireciona automaticamente)
- Revise o Google Analytics ID na tag de rastreamento dos HTMLs
- O arquivo `ads.txt` é servido sem cache para atualização rápida

## 🐛 Troubleshooting

### Arquivo não encontrado
Verifique se o arquivo está na pasta `templates/` com o nome correto

### Erro 500
Verifique os logs do Render (no dashboard) para mais detalhes

### Cache antigo sendo servido
Limpe o cache do navegador (Ctrl+Shift+Delete) ou faça uma requisição com Ctrl+F5