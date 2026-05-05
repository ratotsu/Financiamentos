from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__, static_folder="static")

# Mapeamento de rotas amigáveis para os arquivos HTML
ROUTES = {
    "/": "index.html",
    "/financiamento-carro-usado": "financiamento-carro-usado.html",
    "/financiamento-moto-honda": "financiamento-moto-honda.html",
    "/juros-financiamento-2026": "juros-financiamento-2026.html",
    "/simulador-sem-entrada": "simulador-sem-entrada.html",
    "/ads.txt": "ads.txt.txt",
    "/googlee9e345b2ea532dde.html": "googlee9e345b2ea532dde.html",
}

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")


@app.route("/")
def index():
    return send_from_directory(TEMPLATES_DIR, "index.html")


@app.route("/financiamento-carro-usado")
@app.route("/financiamento-carro-usado.html")
def financiamento_carro_usado():
    return send_from_directory(TEMPLATES_DIR, "financiamento-carro-usado.html")


@app.route("/financiamento-moto-honda")
@app.route("/financiamento-moto-honda.html")
def financiamento_moto_honda():
    return send_from_directory(TEMPLATES_DIR, "financiamento-moto-honda.html")


@app.route("/juros-financiamento-2026")
@app.route("/juros-financiamento-2026.html")
def juros_financiamento_2026():
    return send_from_directory(TEMPLATES_DIR, "juros-financiamento-2026.html")


@app.route("/simulador-sem-entrada")
@app.route("/simulador-sem-entrada.html")
def simulador_sem_entrada():
    return send_from_directory(TEMPLATES_DIR, "simulador-sem-entrada.html")


@app.route("/googlee9e345b2ea532dde.html")
def google_verification():
    return send_from_directory(TEMPLATES_DIR, "googlee9e345b2ea532dde.html")


@app.route("/ads.txt")
def ads_txt():
    return send_from_directory(TEMPLATES_DIR, "ads.txt.txt", mimetype="text/plain")


# Servir arquivos estáticos (CSS, JS, imagens) da pasta static/
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename)


@app.errorhandler(404)
def not_found(e):
    # Tenta servir index como fallback
    return send_from_directory(TEMPLATES_DIR, "index.html"), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)