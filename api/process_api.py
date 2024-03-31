from flask import Blueprint, jsonify, request
from services.process import Service as process_service
from services.user_config import Service as user_config_service

process_blueprint = Blueprint('process', __name__)

@process_blueprint.route('/get', methods=['POST'])
def get_all_process(): 
    """
    查询全部进程，PID、CPU 使用率、内存使用率、完整命令行和命令名
    支持按cpu占用、内存占用排序
    """
    hostname = request.form.get('hostname')
    config = dict(hostname=hostname,dbname="userconfig")
    user_config = user_config_service(config)
    ssh_config = user_config.get_ssh_config_by_hostname()[0]

    network = process_service(ssh_config)
    sort_key = request.form.get('sort_key',"pid")
    res = network.get_all_process(sort_key)
    return res