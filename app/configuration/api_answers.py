from enum import Enum
from dataclasses import dataclass

@dataclass
class server_setup():

    auth_failed_ip: str = 'Wrong server ip.'

    auth_failed_pass: str = 'Wrong server password'
