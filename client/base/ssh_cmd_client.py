import paramiko
from functools import cached_property
import logging
from untils.str_untils import convert_str_base64

class Client:

    def __init__(self,config):
        """
        config[dict]
            -[x]hostname
            -[x]port
            -[x]username
            -[x]password
        """
        self.config = config
    
    @cached_property
    def paramiko_client(self):
        """
        创建ssh客户端连接
        """
        hostname=self.config.get("hostname",None)
        port=self.config.get("port",None)
        username=self.config.get("username",None)
        password=self.config.get("password",None)
        if hostname is None or port is None or username is None or password is None:
            return None
        try:
            paramiko_client = paramiko.SSHClient()
            paramiko_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            paramiko_client.connect(hostname=hostname, port=port, username=username, password=password)
        except paramiko.AuthenticationException:
            logging.error("认证失败，请检查您的用户名或密码")
        except paramiko.SSHException as e:
            logging.error(f"SSH 连接失败：{e}")
        return paramiko_client
    
    def execute_cmd(self,cmd):
        """
        ssh执行命令
        """
        base64_cmd = convert_str_base64(cmd)
        execute_cmd = "sudo echo '{}' | base64 -d | bash".format(base64_cmd)
        stdin, stdout, stderr = self.paramiko_client.exec_command(command=execute_cmd)
        exit_status = stdout.channel.recv_exit_status()
        stdout_output = stdout.read().decode('utf-8')
        stderr_output = stderr.read().decode('utf-8')
        try:
            if "base: command not found" in stderr_output:
                execute_cmd = "sudo echo '{}' | base64 -d | bash".format(cmd)
                stdin, stdout, stderr = self.paramiko_client.exec_command(command=execute_cmd)
                exit_status = stdout.channel.recv_exit_status()
                stdout_output = stdout.read().decode('utf-8')
                stderr_output = stderr.read().decode('utf-8')

            return stdout_output
        except CommandExecutionError as e:
            logging.error(f"命令执行出现错误: {stderr_output}")
    
    def execute_cmd_while(self,count,cmd):
        """
        循环执行ssh执行命令
        """
        cmd = "for i in {{1..{}}}; do {}; sleep 1; done".format(count,cmd)
        base64_cmd = convert_str_base64(cmd)
        execute_cmd = "sudo echo '{}' | base64 -d | bash".format(base64_cmd)
        stdin, stdout, stderr = self.paramiko_client.exec_command(command=execute_cmd)
        exit_status = stdout.channel.recv_exit_status()
        stdout_output = stdout.read().decode('utf-8')
        stderr_output = stderr.read().decode('utf-8')
        try:
            if "base: command not found" in stderr_output:
                execute_cmd = "sudo echo '{}' | base64 -d | bash".format(cmd)
                stdin, stdout, stderr = self.paramiko_client.exec_command(command=execute_cmd)
                exit_status = stdout.channel.recv_exit_status()
                stdout_output = stdout.read().decode('utf-8')
                stderr_output = stderr.read().decode('utf-8')

            if stderr_output or exit_status != 0:
                raise CommandExecutionError(
                    "远程命令执行失败",
                    exit_status=exit_status,
                    stderr_output=stderr_output
                )
            else:
                return stdout_output
        except CommandExecutionError as e:
            logging.error(f"命令执行出现错误: {stderr_output}")

    def execute_cmd_container(self,cmd,container_id):
        """
        在容器内执行命令
        docker exec -e cr={cmd} {container_id} bash -c 'echo $cr|base64 -d|base'
        """
        base64_cmd = convert_str_base64(cmd)
        execute_cmd = "sudo docker exec -e cr={} {} bash -c 'echo $cr|base64 -d|base'".format(base64_cmd,container_id)
        stdin, stdout, stderr = self.paramiko_client.exec_command(command=execute_cmd)
        exit_status = stdout.channel.recv_exit_status()
        stdout_output = stdout.read().decode('utf-8')
        stderr_output = stderr.read().decode('utf-8')
        try:
            if "base: command not found" in stderr_output:
                execute_cmd = "sudo docker exec -e cr={} {} bash -c '$cr'".format(cmd,container_id)
                stdin, stdout, stderr = self.paramiko_client.exec_command(command=execute_cmd)
                exit_status = stdout.channel.recv_exit_status()
                stdout_output = stdout.read().decode('utf-8')
                stderr_output = stderr.read().decode('utf-8')

            if stderr_output or exit_status != 0:
                raise CommandExecutionError(
                    "远程命令执行失败",
                    exit_status=exit_status,
                    stderr_output=stderr_output
                )
            else:
                return stdout_output
        except CommandExecutionError as e:
            logging.error(f"命令执行出现错误: {stderr_output}")

    def close_paramiko_client(self):
        self.paramiko_client.close()

class CommandExecutionError(Exception):
    """自定义异常类，用于命令执行失败时抛出。"""
    def __init__(self, message, exit_status, stderr_output):
        super().__init__(message)
        self.exit_status = exit_status
        self.stderr_output = stderr_output