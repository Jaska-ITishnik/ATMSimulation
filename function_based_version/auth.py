import json
import os
import time
from pathlib import Path

from colorama import Fore, Style

BASE = Path(__file__).parent.parent


def register_card() -> bool:
    card_number = input("💳Karta raqamini kiriting:")
    if len(card_number) != 16:
        print(Fore.RED + Style.BRIGHT + "Karta raqami 16 xonali bo'lishi kerak!")
        time.sleep(4)
        return False
    if not card_number.isdigit():
        print(Fore.RED + Style.BRIGHT + "Karta raqamida faqat raqamlar bo'lishi kerak!")
        time.sleep(4)
        return False
    with open(os.path.join(BASE / "db/data.json"), "r") as db:
        data = json.load(db)
    if card_number in [d["card_number"] for d in data["cards"]]:
        print(Fore.RED + Style.BRIGHT + "Bunday karta allaqachon mavjud!")
        time.sleep(4)
        return False
    return True
