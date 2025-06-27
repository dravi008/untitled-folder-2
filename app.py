import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    CORS(app)
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    from routes.auth import auth_bp
    from routes.students import students_bp
    from routes.logs import logs_bp
    from routes.ai import ai_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(students_bp)
    app.register_blueprint(logs_bp)
    app.register_blueprint(ai_bp)

    @app.route('/')
    def index():
        return {'status': 'FlightDebriefAI backend running!'}

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8080) 