import sys
import os
sys.path.append("/datadrive/scripts_for_nautobot/")
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import csv
import datetime
from netmiko import ConnectHandler
from config import SSH_FAILURES_CSV,GLOBAL_DELAY_FACTOR, CONN_TIMEOUT

class Ssh:
    DEFAAULT_GLOBAL_DELAY_FACTOR = GLOBAL_DELAY_FACTOR
    DEFAULT_CONN_TIMEOUT = CONN_TIMEOUT
    __DEFAULT_SSH_USERNAME = "admin_ssh"
    def __init__( self, ssh_username = None, conn_timeout=None, global_delay_factor = None ):
        self.SSH_FAILURES_CSV = SSH_FAILURES_CSV
        self.__SSH_USERNAME = ssh_username
        self.conn_timeout = conn_timeout
        self.global_delay_factor= global_delay_factor
        if conn_timeout is None:
            self.conn_timeout = self.DEFAULT_CONN_TIMEOUT
        if global_delay_factor is None:
            self.global_delay_factor = self.DEFAAULT_GLOBAL_DELAY_FACTOR
        if ssh_username is None:
            self.__SSH_USERNAME = self.__DEFAULT_SSH_USERNAME
            
        
    def _decrpyt_ssh_password(self):
        load_dotenv('/home/admin_generic/env_file.env')
        SECRET_KEY = os.getenv("SECRET_KEY")
        assert SECRET_KEY
        FERNET = Fernet(SECRET_KEY)
        with open(f"/home/admin_generic/{self.__SSH_USERNAME}_password") as enc_file:
            stored_password = enc_file.read()
        __SSH_PASSWORD = FERNET.decrypt(stored_password).decode()     
        return  __SSH_PASSWORD
     
    def connect( self, hostname, ip_address  ):
        try:
            device = {
                'device_type': 'autodetect',
                'ip': ip_address,
                'username': self.__SSH_USERNAME,
                'password': self._decrpyt_ssh_password(),
                'fast_cli': False,
                'global_delay_factor': self.global_delay_factor, 
                'conn_timeout': self.conn_timeout }
            device_ssh = ConnectHandler(**device)
            device_ssh.enable()
            return device_ssh
            
        except Exception as e:
            with open(self.SSH_FAILURES_CSV, 'a') as ssh_Failures_csv: 
                csv_writer = csv.writer(ssh_Failures_csv)
                timestamp = datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
                csv_writer.writerow([timestamp, hostname, ip_address,str(e).replace('\n', ' ')])   
            ssh_Failures_csv.close() 
            return  str(e).replace('\n', ' ')
        

