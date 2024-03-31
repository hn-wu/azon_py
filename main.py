from flask import Flask
from api.ssh_cmd_api import ssh_cmd_blueprint
from api.user_config_api import user_config_blueprint
from api.network_api import network_blueprint
from api.file_api import file_blueprint

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(ssh_cmd_blueprint, url_prefix='/ssh')
app.register_blueprint(user_config_blueprint, url_prefix='/user/config')
app.register_blueprint(network_blueprint, url_prefix='/network')
app.register_blueprint(file_blueprint, url_prefix='/file')

@app.route('/', methods=['Get'])
def test():
    return "Test Success"

if __name__ == '__main__':
    app.run(debug=True)
