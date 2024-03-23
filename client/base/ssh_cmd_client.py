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
        paramiko_client = paramiko.SSHClient()
        paramiko_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        try:
            hostname=self.config["hostname"]
            port=self.config["port"]
            username=self.config["username"]
            password=self.config["password"]
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
        cmd = self.__convert_base64_cmd__(cmd=cmd)
        stdin, stdout, stderr = self.paramiko_client.exec_command(command=cmd)
        exit_status = stdout.channel.recv_exit_status()
        stdout_output = stdout.read().decode('utf-8')
        stderr_output = stderr.read().decode('utf-8')
        try:
            if stderr_output or exit_status != 0:
                raise CommandExecutionError(
                    "远程命令执行失败",
                    exit_status=exit_status,
                    stderr_output=stderr_output
                )
            else:
                return stdout_output
        except CommandExecutionError as e:
            logging.error(f"命令执行出现错误: {e.message}")

    def __convert_base64_cmd__(self,cmd):
        """
        将cmd转为base64格式的字符串
        """
        if not cmd:
            return None
        base64_cmd = convert_str_base64(cmd)
        cmd = "echo '{}' | base64 -d | bash".format(base64_cmd)
        return cmd

    def close_paramiko_client(self):
        self.paramiko_client.close()

class CommandExecutionError(Exception):
    """自定义异常类，用于命令执行失败时抛出。"""
    def __init__(self, message, exit_status, stderr_output):
        super().__init__(message)
        self.exit_status = exit_status
        self.stderr_output = stderr_output