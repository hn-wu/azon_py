from flask import Blueprint, jsonify, request
from services.user_config import Service as user_config_service

user_config_blueprint = Blueprint('user_config', __name__)

@user_config_blueprint.route('/set', methods=['POST'])
def set_ssh_config():
    """
    -[x]hostname
    -[x]port
    -[x]username
    -[x]password
    """
    hostname = request.form.get('hostname')
    port = request.form.get('port')
    username = request.form.get('username')
    password = request.form.get('password')
    config = dict(hostname=hostname,port=port,
                  username=username,password=password,
                  dbname="userconfig")
    user_config = user_config_service(config)
    user_config.set_ssh_config()

@user_config_blueprint.route('/getbyhostname', methods=['POST'])
def get_ssh_config_by_hostname():
    """
    config[dict]
        -[x]hostname
    """
    hostname = request.form.get('hostname')
    config = dict(hostname=hostname,
                  dbname="userconfig")
    user_config = user_config_service(config)
    res = user_config.get_ssh_config_by_hostname()
    return res