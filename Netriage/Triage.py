import json
from Checkers.ping import ping_device
from Checkers.dns import dns_check
from Checkers.ports import port_check

with open("config.json", "r") as file:
    config_data = json.load(file)
host = config_data["host"]
domain = config_data["domain"]
port = config_data["port"]

def run_netriage():
    print("\nStarting Automated Netriage Suite...\n")

    gateway_status = ping_device(host)
    if gateway_status == False:
        return f"\n Critical Error: Local Network Unreachable"
    else:
        print("\n Ping was succsessful. Checking DNS...")
        dns = dns_check(domain)
        if dns == False:
            print(f"\n{dns}")
            return "DNS Error: DNS is not resolving. Check DNS server settings"
        else:
            print("DNS is resolving properly. Checking port connection...\n")
            p = port_check(domain, port)
            if p == False:
                return "Port Error: Port is closed, check the port settings"
            else:
                return "All layers are functioning as intended"



print(run_netriage())