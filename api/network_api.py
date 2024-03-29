from flask import Blueprint, jsonify, request
from services.network import Service as network_service
from services.ssh_cmd import Service as ssh_cmd_service
from services.user_config import Service as user_config_service

network_blueprint = Blueprint('network', __name__)

@network_blueprint.route('/ip/addr', methods=['POST'])
def get_ip_addr(): 
    """
    查询主机的全部网络配置：网口名、ip、掩码、mac地址、网络接口状态
    -[x]hostname
    """
    hostname = request.form.get('hostname')
    config = dict(hostname=hostname,dbname="userconfig")
    user_config = user_config_service(config)
    ssh_config = user_config.get_ssh_config_by_hostname()[0]

    network = network_service(ssh_config)
    res = network.get_ip_addr()
    return res

@network_blueprint.route('/ip/route', methods=['POST'])
def get_route(): 
    """
    查询主机的全部网络配置：网口名、ip、掩码、mac地址、网络接口状态
    -[x]hostname
    """
    hostname = request.form.get('hostname')
    config = dict(hostname=hostname,dbname="userconfig")
    user_config = user_config_service(config)
    ssh_config = user_config.get_ssh_config_by_hostname()[0]

    network = network_service(ssh_config)
    res = network.get_route()
    return res

@network_blueprint.route('/netstat/port', methods=['POST'])
def get_netstat_port(): 
    """
    查询主机的全部网络配置：网口名、ip、掩码、mac地址、网络接口状态
    -[x]hostname
    """
    hostname = request.form.get('hostname')
    config = dict(hostname=hostname,dbname="userconfig")
    user_config = user_config_service(config)
    ssh_config = user_config.get_ssh_config_by_hostname()[0]

    network = network_service(ssh_config)
    res = network.get_netstat_port()
    return res