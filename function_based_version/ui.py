from function_based_version import welcome_message, logout_message
from function_based_version.auth import register_card


def about_page():
    welcome_tab_choose = input(welcome_message)
    match welcome_tab_choose:
        case "1":
            pass
        case "2":
            if not register_card():
                about_page()
        case "0":
            print(logout_message)
