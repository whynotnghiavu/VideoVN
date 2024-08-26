import logging
from colorama import init, Fore, Style

# Khởi tạo colorama
init(autoreset=True)

# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("history/output.log", encoding="utf-8"),
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
