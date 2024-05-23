import logging
from flask import Flask
from api import create_api

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/")
def root():
    return {"message": "Welcome to the Code Assistant Bot API!"}

# Register blueprints
app.register_blueprint(create_api(), url_prefix='/api')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
