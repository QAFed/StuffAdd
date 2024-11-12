import paramiko
from conf import ConfData

class ModyFile:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def open_ssh_session(self):
        self.ssh.connect(ConfData.IP, username=ConfData.login_ssh, password=ConfData.pass_ssh)

    def close_ssh_session(self):
        self.ssh.close()

    def change_data_in_file_section(self, file_path, section, next_section, subline, new_subline):
        sftp = self.ssh.open_sftp()
        with sftp.open(file_path, 'r') as file:
            string_list = file.readlines()
            in_section = False
            result_str_list = []

            for line in string_list:
                if section in line:
                    in_section = True
                elif next_section in line:
                    in_section = False

                if in_section and subline in line:
                    result_str_list.append(line.replace(subline,new_subline,1))
                else:
                    result_str_list.append(line)

            with sftp.open(file_path, 'w') as file:
                file.writelines(result_str_list)
            sftp.close()

    def activate_oss_in_app_yaml(self):
        self.open_ssh_session()
        self.change_data_in_file_section(ConfData.path_app_yaml,'oss-service:', 'server-info:', 'enabled: false', 'enabled: true')
        self.close_ssh_session()