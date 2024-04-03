from flask import Blueprint, jsonify, request
from services.file import Service as file_service
from services.user_config import Service as user_config_service

file_blueprint = Blueprint('file', __name__)

@file_blueprint.route('/find', methods=['POST'])
def find_file_by_name(): 
    """
    模糊查询，指定文件下的全部文件名
    -[x]addr 查询文件地址目录
    -[x]filename 查询文件名
    """
    data = request.get_json()
    hostname = data.get('hostname')
    config = dict(hostname=hostname,dbname="userconfig")
    user_config = user_config_service(config)
    ssh_config = user_config.get_ssh_config_by_hostname()[0]

    file = file_service(ssh_config)
    addr = data.get('addr')
    filename = data.get('filename')
    res = file.find_file_by_name(addr,filename)
    return res

@file_blueprint.route('/count/word', methods=['POST'])
def find_file_word_count(): 
    """
    查询指定文件中文本出现次数
    -[x]word 查询单词
    -[x]addr 查询文件地址
    """
    hostname = data.get('hostname')
    config = dict(hostname=hostname,dbname="userconfig")
    user_config = user_config_service(config)
    ssh_config = user_config.get_ssh_config_by_hostname()[0]

    file = file_service(ssh_config)
    word = data.get('word')
    addr = data.get('addr')
    res = file.find_file_word_count(word,addr)
    return res