import logging
from datetime import datetime
from colorama import init, Fore, Style

# Khởi tạo colorama
init(autoreset=True)


now = datetime.now()
now = now.strftime("%Y%m%d%H%M%S%f")

# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"history/output{now}.log", encoding="utf-8"),
        # logging.StreamHandler()
    ]
)


class MyLog:
    def title(message):
        logging.warning(message)
        colored_message = f"{Fore.YELLOW}{message}{Style.RESET_ALL}"
        print(colored_message)

    def info(message):
        logging.info(message)
        colored_message = f"{Fore.GREEN}{message}{Style.RESET_ALL}"
        print(colored_message)

    def error(message):
        logging.error(message)
        colored_message = f"{Fore.RED}{message}{Style.RESET_ALL}"
        print(colored_message)
