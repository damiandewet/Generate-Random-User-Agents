import random
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Expanded mapping of operating systems to compatible browsers and rendering engines
OS_BROWSER_MAP: Dict[str, Dict] = {
    "Windows": {
        "os_list": [
            "Windows NT 11.0; Win64; x64",  # Windows 11
            "Windows NT 10.0; Win64; x64",
            "Windows NT 10.0; WOW64",
            "Windows NT 6.3; Win64; x64",   # Windows 8.1
            "Windows NT 6.1; Win64; x64",   # Windows 7
            "Windows NT 6.0; Win32",        # Windows Vista
            "Windows NT 5.1; Win32"         # Windows XP
        ],
        "browsers": {
            "Chrome/105.0.5195.102": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "Firefox/105.0": "Gecko/20100101",
            "Edg/105.0.1343.27": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "OPR/90.0.4480.84": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "Vivaldi/5.4.2753.40": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "Brave/1.43.89": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "Maxthon/6.1.3.3000": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "YaBrowser/22.9.3.779": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "MSIE 11.0": "Trident/7.0"
        }
    },
    "macOS": {
        "os_list": [
            "Macintosh; Intel Mac OS X 13_0",     # macOS Ventura
            "Macintosh; Intel Mac OS X 12_6",     # macOS Monterey
            "Macintosh; Intel Mac OS X 11_6_7",   # macOS Big Sur
            "Macintosh; Intel Mac OS X 10_15_7",  # macOS Catalina
            "Macintosh; Intel Mac OS X 10_14_6"   # macOS Mojave
        ],
        "browsers": {
            "Safari/605.1.15": "AppleWebKit/605.1.15 (KHTML, like Gecko)",
            "Chrome/105.0.5195.102": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "Firefox/105.0": "Gecko/20100101",
            "OPR/90.0.4480.84": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "Vivaldi/5.4.2753.40": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "Brave/1.43.89": "AppleWebKit/537.36 (KHTML, like Gecko)"
        }
    },
    "Linux": {
        "os_list": [
            "X11; Ubuntu; Linux x86_64",
            "X11; Fedora; Linux x86_64",
            "X11; Debian; Linux x86_64",
            "X11; Arch Linux; Linux x86_64",
            "X11; CentOS; Linux x86_64",
            "X11; Red Hat Enterprise Linux; Linux x86_64"
        ],
        "browsers": {
            "Chrome/105.0.5195.102": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "Firefox/105.0": "Gecko/20100101",
            "OPR/90.0.4480.84": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "Vivaldi/5.4.2753.40": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "Brave/1.43.89": "AppleWebKit/537.36 (KHTML, like Gecko)"
        }
    },
    "Android": {
        "os_list": [
            "Linux; Android 13; SM-G998U Build/TP1A.220624.014",
            "Linux; Android 12; Pixel 6 Build/SD2A.210817.036",
            "Linux; Android 11; ONEPLUS A6013 Build/QKQ1.190716.003",
            "Linux; Android 10; HUAWEI ELE-L29 Build/HUAWEIELE-L29",
            "Android 9; Mobile"
        ],
        "browsers": {
            "Chrome/105.0.5195.79 Mobile": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "SamsungBrowser/18.0": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "UCBrowser/14.2.0.1162": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "OPR/64.2.3282.61404": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "DuckDuckGo/7.65.3": "AppleWebKit/537.36 (KHTML, like Gecko)"
        }
    },
    "iOS": {
        "os_list": [
            "iPhone; CPU iPhone OS 16_0 like Mac OS X",
            "iPad; CPU OS 15_6 like Mac OS X",
            "iPod touch; CPU iPhone OS 14_8 like Mac OS X"
        ],
        "browsers": {
            "Mobile Safari/605.1.15": "AppleWebKit/605.1.15 (KHTML, like Gecko)",
            "FxiOS/105.0 Mobile": "AppleWebKit/605.1.15 (KHTML, like Gecko)",
            "DuckDuckGo/7.65.3": "AppleWebKit/605.1.15 (KHTML, like Gecko)"
        }
    },
    "Others": {
        "os_list": [
            "CrOS x86_64 15183.78.0",  # Chrome OS
            "BB10; Touch",             # BlackBerry
            "Linux; U; en-us; KFAUWI Build/KTU84M"  # Kindle Fire
        ],
        "browsers": {
            "Chrome/105.0.5195.102": "AppleWebKit/537.36 (KHTML, like Gecko)",
            "Firefox/105.0": "Gecko/20100101",
            "Safari/534.57.2": "AppleWebKit/534.57.2 (KHTML, like Gecko)",
            "Silk/3.50": "AppleWebKit/537.36 (KHTML, like Gecko)"
        }
    }
}

LOCALIZATION_OPTIONS: List[str] = [
    'en-US', 'en-GB', 'en-CA', 'en-AU', 'en-IN',
    'fr-FR', 'fr-CA', 'fr-BE', 'de-DE', 'de-AT',
    'es-ES', 'es-MX', 'es-AR', 'pt-BR', 'pt-PT',
    'ru-RU', 'ko-KR', 'it-IT', 'nl-NL', 'sv-SE',
    'zh-CN', 'zh-TW', 'ja-JP'
]

def generate_single_user_agent() -> str:
    """
    Generates and returns a single realistic user agent string.
    """
    os_category = random.choice(list(OS_BROWSER_MAP.keys()))
    os_info = OS_BROWSER_MAP[os_category]

    os_part = random.choice(os_info["os_list"])
    browser_part, render_engine = random.choice(list(os_info["browsers"].items()))
    locale = random.choice(LOCALIZATION_OPTIONS)

    user_agent = f"Mozilla/5.0 ({os_part}; {locale}) {render_engine} {browser_part}"
    return user_agent

def generate_multiple_user_agents(n: int) -> List[str]:
    """
    Generates and returns a list of n realistic user agent strings.

    Parameters:
        n (int): The number of user agents to generate.

    Returns:
        List[str]: A list containing n user agent strings.
    """
    user_agents = [generate_single_user_agent() for _ in range(n)]
    return user_agents

def main() -> None:
    """
    Main function to interact with the user.
    """
    while True:
        print("\nUser Agent Generator")
        print("1. Create a single user agent")
        print("2. Create multiple user agents")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            ua = generate_single_user_agent()
            print("\nGenerated User Agent:")
            print(ua)
        elif choice == '2':
            num_input = input("Enter the number of user agents to generate: ").strip()
            try:
                num = int(num_input)
                if num <= 0:
                    raise ValueError("Number must be positive.")
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue

            user_agents = generate_multiple_user_agents(num)
            print(f"\nGenerated {num} User Agents:")
            for ua in user_agents:
                print(ua)

            save_choice = input("\nDo you want to save the user agents to a .txt file? (yes/no): ").strip().lower()
            if save_choice in ['yes', 'y']:
                filename = input("Enter the filename (default 'user_agents.txt'): ").strip()
                if filename == '':
                    filename = 'user_agents.txt'
                try:
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write('\n'.join(user_agents))
                    print(f"User agents saved to '{filename}'.")
                except IOError as e:
                    print(f"An error occurred while saving the file: {e}")
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 0.")

if __name__ == '__main__':
    main()
