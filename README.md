#  Network Automation Pyhon3 Package

## Features implemented
 - Project created with Python Packaging best practices in mind for easy initiation and later publication to pypi.org .
 - All implemented and planned features have OOP for better code reusability via Inheritance, Polymorphism and additional security of credinteals via Encapsulation and Abstraction. 
 - Abstracted SSH connection creation with OOP class usage for  purpose and isolation of password decryption and usage to Ssh class with using Private methods and Data Abstraction.
 - Abstracted log writing capability, on class instantiation the log file path can be defined; for log writing a method can be called and text string passed with optional timestamp.
 
 ## Features Planned
 
 - Integration with Nautobot via DjangoORM / GraphQL RestAPI ; PRTG  RestAPI for object C.R.U.D. and inventory synchronization with Nautobot as SSOT
 - Various use cases of data collection using SSH ; parsing conditionally with regex with actions of configuration change or object creation in inventory  / monitoring solution.

## Instantiating and using utility classes
### SSH Class
####  Brief Description
__SSH_Username is defined in device_interraction\ssh_connect.py > Ssh class for Data Abstraction purpose.
Decryption of credinteals is done through FERNET using paths for secret key / encrypted files defined in Private _decrpyt_ssh_password method.

On instantiation Ssh class accepts following optional parameters: ssh_username , conn_timeout , global_delay_factor. If these are not provided default valuess are assigned in __init__ method.

Once instantiated connect method is used with hostname, ip_address parameters ( __SSH_USERNAME is inherited from  __init__ method.  Exceptions are written into a CSV file with timestamp, hostname, ip_address and error.

### Examples of usage
>  ssh_with_custom_timers  =  Ssh(conn_timeout=120,global_delay_factor=30)
> ssh_with_speciifed_username  =  Ssh(ssh_username="admin_generic")
> ssh_with_default_username_timers  =  Ssh()

  >device_ssh  =  ssh_with_default.connect("hostname","10.0.0.254")
  > device_ssh.send_command("show version")


### Logger class
####  Brief Description
Logger class in utils\log_writer.py accepts log_file_path as parameter on instantiation. Method write accepts message ( str ) parameter and optional force_timestamp ( bool ) for timestamp generation.
#### Examples of usage

> log= Logger(log_file_path="logs/log_file_name.log")
> 
> log.write(message="Text with no timestamp")
> log.write(message="Text with timestamp: ", force_timestamp=True)


# Package installation

 1. Clone from Github  to desired location.
 2. Create new venv for isolation if desired in /desired_location/env/ :

>  python -m venv /desired_location/env/
 3. With /desired_location/ opened install dependencies from pyproject.toml with command:
>  python3 -m pip install .
 5. Generate new FERNET key with and encrypt credinteals ; store encrypted hash in enviorement variables / files:
> Fernet.generate_key()
> utils/encrypt_credinteals.py
6. Define variables in config.py and device_interraction/ssh_connect.py files.