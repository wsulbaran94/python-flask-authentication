from flask import Blueprint, request, jsonify

from services.user_services import UserServices

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
  data = request.get_json()
  response, status = UserServices().register_user(data)
  return jsonify(response), status

@auth_bp.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  response, status = UserServices().login_user(data)
  return jsonify(response), status