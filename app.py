from flask import Flask, send_from_directory, abort, request
import os
import logging
from datetime import datetime

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder="static")

# Configuração para produção
app.config['ENV'] = os.environ.get('FLASK_ENV', 'production')
app.config['DEBUG'] = False
app.config['JSON_SORT_KEYS'] = False

# Mapeamento de rotas amigáveis para os arquivos HTML
ROUTES = {
    "/": "index.html",
    "/financiamento-carro-usado": "financiamento-carro-usado.html",
    "/financiamento-moto-honda": "financiamento-moto-honda.html",
    "/juros-financiamento-2026": "juros-financiamento-2026.html",
    "/simulador-sem-entrada": "simulador-sem-entrada.html",
    "/ads.txt": "ads.txt",
    "/googlee9e345b2ea532dde.html": "googlee9e345b2ea532dde.html",
}

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")

# Middleware para adicionar headers de segurança
@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    
    # Cache control para arquivos estáticos
    if response.mimetype and ('javascript' in response.mimetype or 'css' in response.mimetype or 'image' in response.mimetype):
        response.headers['Cache-Control'] = 'public, max-age=86400'  # 24 horas
    else:
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
    
    return response


@app.route("/")
def index():
    logger.info("Acesso à página inicial")
    return send_from_directory(TEMPLATES_DIR, "index.html")


@app.route("/financiamento-carro-usado")
@app.route("/financiamento-carro-usado.html")
def financiamento_carro_usado():
    logger.info("Acesso à página de financiamento de carro usado")
    return send_from_directory(TEMPLATES_DIR, "financiamento-carro-usado.html")


@app.route("/financiamento-moto-honda")
@app.route("/financiamento-moto-honda.html")
def financiamento_moto_honda():
    logger.info("Acesso à página de financiamento de moto Honda")
    return send_from_directory(TEMPLATES_DIR, "financiamento-moto-honda.html")


@app.route("/juros-financiamento-2026")
@app.route("/juros-financiamento-2026.html")
def juros_financiamento_2026():
    logger.info("Acesso à página de juros de financiamento 2026")
    return send_from_directory(TEMPLATES_DIR, "juros-financiamento-2026.html")


@app.route("/simulador-sem-entrada")
@app.route("/simulador-sem-entrada.html")
def simulador_sem_entrada():
    logger.info("Acesso ao simulador sem entrada")
    return send_from_directory(TEMPLATES_DIR, "simulador-sem-entrada.html")


@app.route("/googlee9e345b2ea532dde.html")
def google_verification():
    logger.info("Verificação Google")
    return send_from_directory(TEMPLATES_DIR, "googlee9e345b2ea532dde.html")


@app.route("/ads.txt")
def ads_txt():
    logger.info("Acesso a ads.txt")
    return send_from_directory(TEMPLATES_DIR, "ads.txt", mimetype="text/plain")


# Servir arquivos estáticos (CSS, JS, imagens) da pasta static/
@app.route("/static/<path:filename>")
def static_files(filename):
    try:
        return send_from_directory(app.static_folder, filename)
    except FileNotFoundError:
        logger.warning(f"Arquivo estático não encontrado: {filename}")
        abort(404)


@app.errorhandler(404)
def not_found(e):
    logger.warning(f"Erro 404: {e}")
    # Tenta servir index como fallback
    return send_from_directory(TEMPLATES_DIR, "index.html"), 404


@app.errorhandler(500)
def internal_error(e):
    logger.error(f"Erro 500: {e}", exc_info=True)
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Erro 500 - Servidor</title>
        <style>
            body { font-family: Arial; text-align: center; padding: 50px; background: #f5f7fb; }
            .error { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
            h1 { color: #dc3545; }
        </style>
    </head>
    <body>
        <div class="error">
            <h1>Erro 500</h1>
            <p>Desculpe, ocorreu um erro no servidor. Tente novamente mais tarde.</p>
        </div>
    </body>
    </html>
    """, 500


@app.before_request
def log_request_info():
    logger.debug(f"Requisição: {request.method} {request.path}")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    logger.info(f"Iniciando aplicação Flask em {host}:{port}")
    logger.info(f"Ambiente: {app.config['ENV']}")
    app.run(host=host, port=port, debug=False)