from flask import Blueprint, jsonify, request
from services.ssh_cmd import Service as ssh_cmd_service
from services.user_config import Service as user_config_service

ssh_cmd_blueprint = Blueprint('ssh_cmd', __name__)

@ssh_cmd_blueprint.route('/cmd', methods=['POST'])
def execute_cmd(): 
    """
    ssh执行命令
    """
    hostname = request.form.get('hostname')
    dbname = request.form.get('dbname')
    config = dict(hostname=hostname,dbname=dbname)
    user_config = user_config_service(config)
    ssh_config = user_config.get_ssh_config_by_hostname()

    cmd = request.form.get('cmd')
    ssh_cmd = ssh_cmd_service(ssh_config)
    res = ssh_cmd.execute_cmd(cmd)
    return res

@ssh_cmd_blueprint.route('/cmdContainer', methods=['POST'])
def execute_cmd_container():
    """
    在容器内执行命令
    """
    hostname = request.form.get('hostname')
    dbname = request.form.get('dbname')
    config = dict(hostname=hostname,dbname=dbname)
    user_config = user_config_service(config)
    ssh_config = user_config.get_ssh_config_by_hostname()

    cmd = request.form.get('cmd')
    container_id = request.form.get('container_id')
    ssh_cmd = ssh_cmd_service(ssh_config)
    res = ssh_cmd.execute_cmd_container(cmd,container_id)
    return res