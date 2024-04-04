from flask import Blueprint, jsonify, request
from services.ssh_cmd import Service as ssh_cmd_service
from services.user_config import Service as user_config_service

ssh_cmd_blueprint = Blueprint('ssh_cmd', __name__)

@ssh_cmd_blueprint.route('/cmd', methods=['POST'])
def execute_cmd(): 
    """
    ssh执行命令
    -[x]hostname
    """
    data = request.get_json()
    hostname = data.get('hostname')
    config = dict(hostname=hostname,dbname="userconfig")
    user_config = user_config_service(config)
    ssh_config = user_config.get_ssh_config_by_hostname()[0]

    cmd = data.get('cmd')
    ssh_cmd = ssh_cmd_service(ssh_config)
    res = ssh_cmd.execute_cmd(cmd)
    return res

@ssh_cmd_blueprint.route('/cmd/while', methods=['POST'])
def execute_cmd_while(): 
    """
    循环ssh执行命令
    -[x]hostname
    TODO补充响应码，显示对应结果
    """
    data = request.get_json()
    hostname = data.get('hostname')
    config = dict(hostname=hostname,dbname="userconfig")
    user_config = user_config_service(config)
    ssh_config = user_config.get_ssh_config_by_hostname()[0]

    count = data.get('count')
    cmd = data.get('cmd')
    ssh_cmd = ssh_cmd_service(ssh_config)
    res = ssh_cmd.execute_cmd_while(count,cmd)
    return res

@ssh_cmd_blueprint.route('/cmdContainer', methods=['POST'])
def execute_cmd_container():
    """
    在容器内执行命令
    -[x]hostname
    """
    data = request.get_json()
    hostname = data.get('hostname')
    config = dict(hostname=hostname,dbname="userconfig")
    user_config = user_config_service(config)
    ssh_config = user_config.get_ssh_config_by_hostname()[0]

    cmd = data.get('cmd')
    container_id = data.get('container_id')
    ssh_cmd = ssh_cmd_service(ssh_config)
    res = ssh_cmd.execute_cmd_container(cmd,container_id)
    return res