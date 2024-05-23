from flask import Flask, request, jsonify
from flask_restful import Api
from api import codellama_bp, gpt_bp
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
api = Api(app)

# Register Blueprints
app.register_blueprint(codellama_bp, url_prefix='/codellama')
app.register_blueprint(gpt_bp, url_prefix='/gpt')

@app.route('/')
def root():
    return jsonify({"message": "Welcome to the Code Assistant Bot API!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
