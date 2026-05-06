#!/bin/bash
# Script de setup rápido - use este script para preparar o ambiente localmente

echo "🚀 Preparando ambiente de desenvolvimento..."

# Criar ambiente virtual
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python -m venv venv
fi

# Ativar ambiente virtual
echo "⚡ Ativando ambiente virtual..."
source venv/bin/activate  # No Windows use: venv\Scripts\activate

# Instalar dependências
echo "📚 Instalando dependências..."
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Criar arquivo .env se não existir
if [ ! -f ".env" ]; then
    echo "📝 Criando arquivo .env..."
    cp .env.example .env
    echo "ℹ️  Edite o arquivo .env com suas configurações"
fi

echo ""
echo "✅ Setup concluído!"
echo ""
echo "Para iniciar a aplicação, execute:"
echo "  python app.py"
echo ""
echo "A aplicação estará disponível em: http://localhost:5000"
echo ""
