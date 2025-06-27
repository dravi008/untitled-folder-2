import os
 
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///flightdebriefai.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET', 'super-secret')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '') 