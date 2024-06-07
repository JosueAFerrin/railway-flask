from flask import Flask

def create_app():
    app = Flask(__name__)
    
    with app.app_context():
        from . import routes  # Importa las rutas desde routes.py
        app.register_blueprint(routes.bp)  # Registra el blueprint
        
        return app
