
from common.services.handle_error import HandleErrorsService
from models.user import User, db
from schemas.login_schema import LoginSchema
from schemas.user_schema import UserSchema


class UserServices:
  user_schema = UserSchema()
  login_schema = LoginSchema()
  
  def handle_error_user(self, error, statusCode=None):
    return HandleErrorsService(error, statusCode).get_error()
  
  def register_user(self, user):
    errors = self.user_schema.validate(user)
    if errors:
      return self.handle_error_user({"status": "fail", "message": errors}, 400)
    
    username = user.get("username")
    email = user.get("email")
    password = user.get("password")
    
    if(User.query.filter_by(username=username).first()):
      return self.handle_error_user({"status": "fail", "message": "Username already exists"}, 409)
    if(User.query.filter_by(email=email).first()):
      return self.handle_error_user({"status": "fail", "message": "Email already exists"}, 409)
    
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return {"status": "success", "message": "User created successfully"}, 201
  
  def login_user(self, user):
    errors = self.login_schema.validate(user)
    if errors:
      return self.handle_error_user({"status": "fail", "message": errors}, 400)
    
    username = user.get("username")
    password = user.get("password")
    
    user = User.query.filter_by(username=username).first()
    
    if not user or not user.check_password(password):
      return self.handle_error_user({"status": "fail", "message": "Invalid username or password"}, 401)
    
    return {"status": "success", "message": "Login successful"}, 200