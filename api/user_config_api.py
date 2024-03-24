from flask import Blueprint, jsonify, request
from services.user_config import Service as user_config_service

user_config_blueprint = Blueprint('user_config', __name__)

@user_config_blueprint.route('/set/ssh/config', methods=['POST'])
def set_ssh_config():
    """
    config[dict]
        -[x]hostname
        -[x]port
        -[x]username
        -[x]password
        -[x]dbname
    """
    config = request.form.get('config')
    user_config = user_config_service(config)
    user_config.set_ssh_config()

@user_config_blueprint.route('/get/ssh/config/hostname', methods=['POST'])
def get_ssh_config_by_hostname():
    """
    config[dict]
        -[x]hostname
        -[x]port
        -[x]username
        -[x]password
        -[x]dbname
    """
    config = request.form.get('config')
    user_config = user_config_service(config)
    res = user_config.get_ssh_config_by_hostname()
    return res