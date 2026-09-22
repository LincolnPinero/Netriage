import socket
def port_check(target_domain, target_port):
    s = socket.socket()
    s.settimeout(2.0)
    if s.connect_ex((target_domain, target_port)) == 0:
        print(f"\nConnection was succsessful, Port {target_port} is OPEN")
        return True
    else:
        print(f"\nConnection failed, Port {target_port} is CLOSED")
        return False
