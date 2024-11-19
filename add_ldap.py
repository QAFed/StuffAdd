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
    ssh.send_command(f'scp -o StrictHostKeyChecking=no {ConfData.main_login}@{ConfData.main_ip}:"{ConfData.ldap_conf}/ldap_conf.xml" .')
    ssh.send_command(ConfData.main_pass)
    ssh.send_command("rm /srv/pl-services/staff-service/ldap_conf.xml")
    ssh.send_command("mv ldap_conf.xml /srv/pl-services/staff-service/")
    ssh.send_command("sed -i '/ldap-host:/c\    ldap-host: 192.168.62.120' /srv/pl-services/postlink-service/config/application.yaml")
    ssh.send_command(
        "sed -i '/ldap-port:/c\    ldap-port: 389' /srv/pl-services/postlink-service/config/application.yaml")
    ssh.send_command(
        "sed -i '/ldap-user-name-mask:/c\    ldap-user-name-mask: uid=%userName%,ou=AfroTestUsers,dc=stc-tst,dc=local' /srv/pl-services/postlink-service/config/application.yaml")
    ssh.send_command(
        "sed -i '/oss-service:/,/^server-info:/s/enabled: false/enabled: true/' /srv/pl-services/postlink-service/config/application.yaml")
    ssh.send_command("systemctl restart pl admin staff")
    time.sleep(5)
    ssh.stop_shell()
    ssh.ssh_disconnect()