from colorama import Fore, Style

from function_based_version import welcome_message, logout_message, main_menu_message
from function_based_version.auth import register_card, login_card


def about_page():
    welcome_tab_choose = input(welcome_message)
    match welcome_tab_choose:
        case "1":
            if not login_card():
                about_page()
            else:
                print(Fore.GREEN + Style.BRIGHT + "Akountga xush kelibsiz🎉")
                print(main_menu_message("acc_1"))
        case "2":
            if not register_card():
                about_page()
            else:
                print(Fore.GREEN + Style.BRIGHT + "Karta muvofaqiyatliy yaratildi🎉")
                about_page()
        case "0":
            print(logout_message)


"""

git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
"""