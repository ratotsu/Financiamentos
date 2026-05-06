# 🚀 GUIA RÁPIDO DE DEPLOY

## 1️⃣ Verificação Rápida (2 minutos)

```bash
# Abra o terminal na pasta do projeto
cd c:\Users\will\Documents\GitHub\Financiamentos

# Teste a aplicação
python test_app.py

# Você deve ver: ✓ Tudo OK! Pronto para produção
```

## 2️⃣ Rodar Localmente (5 minutos)

### Windows
```bash
setup.bat
python app.py
```

### Mac/Linux
```bash
bash setup.sh
python app.py
```

Acesse: http://localhost:5000

## 3️⃣ Deploy no Render (2 minutos)

### Passo 1: Fazer Push
```bash
git add .
git commit -m "Preparar projeto para produção"
git push origin main
```

### Passo 2: Deploy
1. Vá para https://render.com
2. Clique em "New +" → "Web Service"
3. Selecione seu repositório
4. Render detecta `render.yaml` automaticamente
5. Clique em "Deploy"

### Passo 3: Pronto!
- Site em: `https://<seu-app>.onrender.com`
- Logs em: Render Dashboard

## 🆘 Problemas Comuns

### "ModuleNotFoundError: No module named 'flask'"
```bash
pip install -r requirements.txt
```

### "Porta 5000 já está em uso"
```bash
# Windows
netstat -ano | findstr :5000

# Mac/Linux
lsof -i :5000
```

### "Arquivo não encontrado"
Verifique se está em `templates/` com nome correto

### "Erro 500 no Render"
Vá ao Dashboard → Logs e procure a mensagem de erro

## 📞 Suporte Rápido

| Problema | Solução |
|----------|---------|
| Erro local | Rode `python test_app.py` |
| Cache antigo | Limpe com Ctrl+Shift+Del |
| Deploy falhou | Verifique os logs do Render |
| Lentidão | Revise `PRODUCAO_CHECKLIST.md` |

---

**Tempo total:** ~10 minutos para deploy
