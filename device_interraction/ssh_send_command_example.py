import sys
import os
# sys.path.append("/datadrive/scripts_for_nautobot/")
os.chdir("/datadrive/scripts_for_nautobot/")
from ssh_connect import Ssh
from utils.log_writer import Logger

log = Logger(log_file_path="logs/ssh_get_l3_interface.log")
log.write(message="Text with no timestamp")
log.write(message="Text with timestamp: ", force_timestamp=True)

ssh_with_custom_timers = Ssh(conn_timeout=120,global_delay_factor=30)
ssh_with_speciifed_username = Ssh(ssh_username="admin_generic")
ssh_with_default = Ssh()



device_ssh = ssh_with_default.connect("bbro501","10.114.17.254")
print(device_ssh.send_command("show version"))