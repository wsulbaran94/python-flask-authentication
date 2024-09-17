from flask import Flask
from models.user import db
from blueprints.auth.routes import auth_bp
from configuration import config
app = Flask(__name__)

# config db
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# config db
app.config.from_object(config['development'])

# init db
db.init_app(app)

#create tables
with app.app_context():
  db.create_all()
  
# Register the blueprint
app.register_blueprint(auth_bp, url_prefix='/api/auth')


if __name__ == '__main__':
  app.run(debug=True)