# gerador_api_flask/src/main.py
import os
import sys
from flask import Flask
from flask_cors import CORS

# Adicionar o diretório src ao sys.path para permitir importações absolutas de módulos dentro de src
# Isso é crucial para a estrutura do projeto Flask que o Render.com espera.
# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Para acessar a raiz do projeto se main.py estiver em src/

# Correção para garantir que o diretório pai de 'src' (ou seja, a raiz do projeto Flask) esteja no sys.path
# Isso permite que 'from src.routes... import ...' funcione corretamente.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from src.routes.gerador_pecas_route import gerador_pecas_bp

app = Flask(__name__)

# Configurar CORS para permitir todas as origens. 
# Para produção, restrinja às origens do seu frontend Next.js.
CORS(app) # Isso permitirá todas as origens por padrão
# Exemplo de configuração mais restrita:
# cors = CORS(app, resources={r"/api/*": {"origins": "https://your-nextjs-app-domain.onrender.com"}})

app.register_blueprint(gerador_pecas_bp)

@app.route("/")
def health_check():
    return "Gerador de Peças API está funcionando!"

if __name__ == "__main__":
    # Render.com usará um servidor WSGI como Gunicorn, então esta parte é mais para desenvolvimento local.
    # Render define a variável de ambiente PORT.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True) # debug=False para produção

