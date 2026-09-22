import json
import os
import sys
from Checkers.ping import ping_device
from Checkers.dns import dns_check
from Checkers.ports import port_check
import colorama
from colorama import Fore, Style, init
init(autoreset=True)

if hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

config_path = os.path.join(base_path, "config.json")

with open(config_path, "r") as file:
    config_data = json.load(file)

host = config_data["host"]
domain = config_data["domain"]
port = config_data["port"]


def run_netriage():
    print(f"\n{Fore.CYAN}{Style.BRIGHT}Starting Automated Netriage Suite...\n")

    gateway_status = ping_device(host)
    if gateway_status == False:
        print(f"\n {Fore.RED}{Style.BRIGHT}Critical Error: Local Network Unreachable")
        return False
    else:
        print(f"\n {Fore.GREEN}Ping was successful. {Fore.YELLOW}Checking DNS...")
        dns = dns_check(domain)
        if dns == False:
            print(f"{Fore.RED}DNS Error: DNS is not resolving. Check DNS server settings")
            return False
        else:
            print(f"{Fore.GREEN}DNS is resolving properly. {Fore.YELLOW}Checking port connection...\n")
            p = port_check(domain, port)
            if p == False:
                print(f"{Fore.RED}Port Error: Port is closed, check the port settings")
                return False
            else:
                print(f"{Fore.GREEN}{Style.BRIGHT}All layers are functioning as intended")
                return True


def main_menu():
    while True:
        os.system("cls" if os.name == 'nt' else 'clear')
        print(f"\n{Fore.BLUE}{Style.BRIGHT}=== NETRIAGE DIAGNOSTIC TOOL ===")
        print("1. Run Automated Triage")
        print("2. Test Custom IP or Domain")
        print("3. View Loaded Network Configuration")
        print(f"{Fore.RED}4. Exit Netriage")

        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            run_netriage()
            input("\nDiagnostic complete. Press Enter to return to menu...")

        elif choice == "2":
            custom_target = input("\nEnter target IP or Domain (8.8.8.8 or google.com): ").strip()
            if custom_target:
                print(f"\n{Fore.YELLOW}Running custom test on {custom_target}...")
                ping_device(custom_target)
                dns_check(custom_target)
                port_check(custom_target, 80)
                input("\nCustom test complete. Press Enter to return to main menu...")

        elif choice == "3":
            print(f"\n{Fore.YELLOW}--- Current Loaded Configuration ---")
            print(json.dumps(config_data, indent=2))
            input("\nPress Enter to return to main menu...")

        elif choice == "4":
            print(f"\n{Fore.YELLOW}Shutting Netriage down. Goodbye!")
            break
        else:
            print(f"\n{Fore.RED}Invalid option. Select in the range of (1-4)")
            input("Press Enter to return to menu...")


if __name__ == "__main__":
    main_menu()
