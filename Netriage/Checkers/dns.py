import socket
from colorama import Fore, Style, init
init(autoreset=True)
def dns_check(domain):
    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror as e:
        return f"Network or DNS Error Occured {e}{Style.RESET_ALL}"

    pass
