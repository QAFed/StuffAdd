import paramiko
import time
from conf import ConfData


class SshConnect:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    shell = None

    def ssh_connect(self, host, login, passw):
        self.ssh.connect(hostname=host, username=login, password=passw)

    def ssh_disconnect(self):
        self.ssh.close()

    def start_shell(self):
        self.shell = self.ssh.invoke_shell()

    def stop_shell(self):
        self.shell.close()

    def send_command(self, command):
        # print(f'SEND COMMAND {command}')
        self.shell.send(command + '\n')
        time.sleep(1)
        output = ""
        while True:
            if self.shell.recv_ready():
                response = self.shell.recv(1024).decode('utf-8', errors='replace')
                output += response
                print(response, end='')
                time.sleep(1)

                if output.endswith("$ ") or output.endswith("# ") or output.endswith(f"{ConfData.login_ssh}: ") or output.endswith("password: "):
                    break
