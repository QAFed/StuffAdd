from mody_file.inter_cli import SshConnect
from conf import ConfData
import time


if __name__ == '__main__':
    ssh = SshConnect()
    ssh.ssh_connect(ConfData.IP, ConfData.login_ssh, ConfData.pass_ssh)
    ssh.start_shell()
    ssh.send_command('hostname -I')
    ssh.send_command('sudo -s')
    ssh.send_command(ConfData.pass_ssh)
    ssh.send_command(f'scp -o StrictHostKeyChecking=no {ConfData.main_login}@{ConfData.main_ip}:"{ConfData.ssh_sert_temp_folder}/password.pass" .')
    ssh.send_command(ConfData.main_pass)
    ssh.send_command(f'scp -o StrictHostKeyChecking=no {ConfData.main_login}@{ConfData.main_ip}:"{ConfData.ssh_sert_temp_folder}/certificate.pfx" .')
    ssh.send_command(ConfData.main_pass)
    ssh.send_command("rm -r /srv/pl-services/postlink-service/oss")
    ssh.send_command("mkdir /srv/pl-services/postlink-service/oss")
    ssh.send_command("mv password.pass /srv/pl-services/postlink-service/oss/")
    ssh.send_command("mv certificate.pfx /srv/pl-services/postlink-service/oss/")
    ssh.send_command("sed -i '/oss-service:/,/^server-info:/s/enabled: false/enabled: true/' /srv/pl-services/postlink-service/config/application.yaml")
    time.sleep(5)
    ssh.stop_shell()
    ssh.ssh_disconnect()
