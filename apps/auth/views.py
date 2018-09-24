from flask import Blueprint, request, current_app


auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['GET'])
def login():
    return 'true un auth'
