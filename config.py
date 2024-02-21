import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv


# General
PACKAGE_DIR = "/datadrive/scripts_for_nautobot/"


# Credinteals
load_dotenv('/home/admin_generic/nautobot.env')
SECRET_KEY = os.getenv("SECRET_KEY")
assert SECRET_KEY
FERNET = Fernet(SECRET_KEY)

# def get_password():
#     with open("/home/admin_generic/admin_ssh_password") as enc_file:
#         stored_password = enc_file.read()
#     SSH_PASSWORD = FERNET.decrypt(stored_password).decode()
#     return SSH_PASSWORD
# SSH_PASSWORD = get_password()

def get_token():
    with open("/home/admin_generic/nautobot_token") as enc_file_token:
        stored_token = enc_file_token.read()
    TOKEN = FERNET.decrypt(stored_token).decode()
    return TOKEN
TOKEN = get_token()

# Log file paths:
SSH_FAILURES_CSV = "/datadrive/scripts_for_nautobot/logs/SSH_Failures.csv"

# SSH Options:
GLOBAL_DELAY_FACTOR = 3
CONN_TIMEOUT = 90