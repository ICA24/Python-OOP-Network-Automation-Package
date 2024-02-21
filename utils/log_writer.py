import datetime

class Logger:
    def __init__(self,log_file_path):
        self.timestamp = None
        self.log_file_path = log_file_path
    def write(self, message : str, force_timestamp: bool = False) -> None:
        if not force_timestamp:
            log_message = message
        else:
            log_message = message + " " + datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
        with open(self.log_file_path, 'a') as file:
            file.write(log_message + '\n')
            file.close()


