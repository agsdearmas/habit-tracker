import os
from flask import Flask
from app.services import services
from dotenv import load_dotenv

load_dotenv()


# Inicializar los servicios
def init_services(app):
    for service in services:
        service.init_app(app)


def create_app(config_class=None):
    app = Flask(__name__)

    # Seleccionar configuracion segon entorno
    env = os.getenv('FLASK_ENV', 'default')

    if not config_class:
        if env == 'production':
            from app.settings import ProductionConfig
            config_class = ProductionConfig
        elif env == 'develop':
            from app.settings import DevelopConfig
            config_class = DevelopConfig
        elif env == 'staging':
            from app.settings import StagingConfig
            config_class = StagingConfig
        elif env == 'analytics':
            from app.settings import AnalyticsConfig
            config_class = AnalyticsConfig
        elif env == 'testing':
            from app.settings import TestingConfig
            config_class = TestingConfig
        else:
            from app.settings import DefaultConfig
            config_class = DefaultConfig

    app.config.from_object(config_class)

    # Inicializar servicios
    init_services(app)

    # Registrar blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.health_routes import health_bp
    # from app.routes.habito_routes import habito_bp
    # from app.routes.registro_routes import registro_bp
    # from app.routes.reporte_routes import reporte_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(health_bp, url_prefix='/healthcheck')
    # app.register_blueprint(habito_bp, url_prefix='/habitos')
    # app.register_blueprint(registro_bp, url_prefix='/registros')
    # app.register_blueprint(reporte_bp, url_prefix='/reportes')

    return app