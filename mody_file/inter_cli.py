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
                response = self.shell.recv(1024).decode('utf-8')
                output += response
                print(f'RESPONSE {response}', end='')
                time.sleep(1)

                if output.endswith("$ ") or output.endswith("# "):
                    break

if __name__ == '__main__':
    ssh = SshConnect()
    ssh.ssh_connect(ConfData.IP, ConfData.login_ssh, ConfData.pass_ssh)
    ssh.start_shell()
    ssh.send_command('hostname -I')
    ssh.send_command('sudo -s')
    ssh.send_command(ConfData.login_ssh)
    ssh.send_command('apt update -y')
    time.sleep(5)
    ssh.stop_shell()
    ssh.ssh_disconnect()





