# Changelog

## [Produção v1.0] - 2026-05-05

### ✨ Adicionado
- Logging completo de requisições e erros
- Headers de segurança HTTP (X-Frame-Options, Content-Type-Options, etc.)
- Cache control inteligente para otimização de performance
- Tratamento robusto de erros 404 e 500
- Suporte a variáveis de ambiente (.env)
- Arquivo .gitignore para Python
- Configuração melhorada do render.yaml com health check
- Procfile para compatibilidade com Heroku/Render
- runtime.txt com especificação de Python
- Documentação completa de produção
- Checklist de pré-deploy
- Testes básicos da aplicação
- requirements-dev.txt para ferramentas de desenvolvimento

### 🔧 Alterado
- Melhorado app.py com middleware de segurança
- Atualizado README.md com instruções completas
- Renomeado ads.txt.txt para ads.txt
- Melhorado render.yaml com 4 workers e timeout de 120s
- requirements.txt agora inclui python-dotenv

### 🔒 Segurança
- Headers X-Content-Type-Options: nosniff
- Headers X-Frame-Options: SAMEORIGIN
- Headers X-XSS-Protection ativo
- Referrer-Policy: strict-origin-when-cross-origin
- Logging de erros com exc_info
- Sem expõem de stack traces em produção

### 📊 Performance
- Cache de 24 horas para arquivos estáticos
- No-cache para páginas HTML
- Gunicorn com 4 workers
- Timeout aumentado para 120 segundos

### 📝 Documentação
- README.md expandido com 200+ linhas
- PRODUCAO_CHECKLIST.md com guia pré-deploy
- Código comentado e bem estruturado
- Exemplos de uso (.env.example)
