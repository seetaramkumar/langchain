from flask import Blueprint
from api.codellama import router as codellama_router
from api.gpt import router as gpt_router

def create_api():
    api = Blueprint('api', __name__)
    api.register_blueprint(codellama_router, url_prefix='/codellama')
    api.register_blueprint(gpt_router, url_prefix='/gpt')
    print("in create API", api)
    return api
