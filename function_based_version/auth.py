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
        print(Fore.RED + Style.BRIGHT + "PIN kodlar mos kelmadi")
        time.sleep(2)
        check_pin_code()
    else:
        return pin_code


def card_validator(card_number: str):
    if not card_number.isdigit():
        print(Fore.RED + Style.BRIGHT + "Karta raqamida faqat raqamlar bo'lishi kerak!")
        time.sleep(4)
        return False
    if len(card_number) != 16:
        print(Fore.RED + Style.BRIGHT + "Karta raqami 16 xonali bo'lishi kerak!")
        time.sleep(4)
        return False


def register_card() -> bool:
    card_number = input("💳Karta raqamini kiriting:")
    card_validator(card_number)
    with open(os.path.join(BASE / "db/data.json"), "r") as db:  # new
        data = json.load(db)

    if card_number in [d["card_number"] for d in data["cards"]]:
        print(Fore.RED + Style.BRIGHT + "Bunday karta allaqachon mavjud!")
        time.sleep(4)
        return False
    pin_code = check_pin_code()
    last_account = [d["account_id"] for d in data["cards"]][-1]
    account_id = f"acc_{int(last_account[-1]) + 1}"
    owner = input(Fore.GREEN + Style.BRIGHT + "To'liq ism ni kiriting:")
    with open(os.path.join(BASE / "db/data.json"), "w") as db:  # new
        data["accounts"].append({
            "account_id": account_id,
            "balance": 0,
            "currency": "UZS"
        })
        data["cards"].append({
            "card_number": card_number,
            "pin": pin_code,
            "account_id": account_id,
            "owner": owner,
            "blocked": False,
            "pin_tries": 0
        })
        json.dump(data, db, indent=3)
    return True


def login_card() -> bool:  # noqa
    card_number = input("💳Karta raqamini kiriting:")
    card_validator(card_number)
    with open(os.path.join(BASE / "db/data.json"), "r") as db:  # new
        data = json.load(db)

    if card_number not in [d["card_number"] for d in data["cards"]]:
        print(Fore.RED + Style.BRIGHT + "Bunday karta mavjud emas!")
        time.sleep(3)
        return False
    return True