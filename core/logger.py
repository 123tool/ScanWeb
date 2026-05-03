from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(f"{Fore.CYAN}{Style.BRIGHT}" + "="*45)
    print(f"{Fore.WHITE}      SPY-E SECURITY RESEARCH PRO")
    print(f"{Fore.CYAN}    Automated Audit & Discovery Tool")
    print(f"{Fore.CYAN}{Style.BRIGHT}" + "="*45 + "\n")

def log_info(msg):
    print(f"{Fore.BLUE}[INFO] {Fore.WHITE}{msg}")

def log_success(msg):
    print(f"{Fore.GREEN}[FOUND] {Fore.WHITE}{msg}")

def log_warn(msg):
    print(f"{Fore.YELLOW}[WARN] {Fore.WHITE}{msg}")
