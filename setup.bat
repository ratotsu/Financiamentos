@echo off
REM Script de setup rápido para Windows

echo.
echo 🚀 Preparando ambiente de desenvolvimento...
echo.

REM Criar ambiente virtual
if not exist "venv" (
    echo 📦 Criando ambiente virtual...
    python -m venv venv
)

REM Ativar ambiente virtual
echo ⚡ Ativando ambiente virtual...
call venv\Scripts\activate

REM Instalar dependências
echo 📚 Instalando dependências...
pip install -r requirements.txt
pip install -r requirements-dev.txt

REM Criar arquivo .env se não existir
if not exist ".env" (
    echo 📝 Criando arquivo .env...
    copy .env.example .env
    echo ℹ️  Edite o arquivo .env com suas configurações
)

echo.
echo ✅ Setup concluído!
echo.
echo Para iniciar a aplicação, execute:
echo   python app.py
echo.
echo A aplicação estará disponível em: http://localhost:5000
echo.
pause
