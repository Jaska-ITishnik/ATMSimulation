import json
import os
import time
from pathlib import Path

from colorama import Fore, Style

BASE = Path(__file__).parent.parent


def check_pin_code():
    pin_code = input("🔢PIN kod o'rnating:")
    confirm_pin = input("🔢PIN kod ni qayta kiriting:")
    while pin_code != confirm_pin:
        check_pin_code()
    else:
        return pin_code


def check_owner():
    owner = input("Karta kim uchun:")


def register_card() -> bool:
    card_number = input("💳Karta raqamini kiriting:")
    if not card_number.isdigit():
        print(Fore.RED + Style.BRIGHT + "Karta raqamida faqat raqamlar bo'lishi kerak!")
        time.sleep(4)
        return False
    if len(card_number) != 16:
        print(Fore.RED + Style.BRIGHT + "Karta raqami 16 xonali bo'lishi kerak!")
        time.sleep(4)
        return False

    with open(os.path.join(BASE / "db/data.json"), "r") as db:
        data = json.load(db)

    if card_number in [d["card_number"] for d in data["cards"]]:
        print(Fore.RED + Style.BRIGHT + "Bunday karta allaqachon mavjud!")
        time.sleep(4)
        return False
    pin_code = check_pin_code()
    last_account = [d["account_id"] for d in data["cards"]][-1]
    account_id = f"acc_{int(last_account["account_id"].split("_")[-1]) + 1}"
    return True
