import time
import pyautogui

from faker import Faker
from pynput.keyboard import Key, Controller

fake = Faker()
Faker.seed(0)

keyboard = Controller()

print("""
 ____  _______     _____ ____ _____      _    ____  ____  _____ ____  
|  _ \| ____\ \   / /_ _/ ___| ____|    / \  |  _ \|  _ \| ____|  _ \ 
| | | |  _|  \ \ / / | | |   |  _|     / _ \ | | | | | | |  _| | |_) |
| |_| | |___  \ V /  | | |___| |___   / ___ \| |_| | |_| | |___|  _ < 
|____/|_____|  \_/  |___\____|_____| /_/   \_\____/|____/|_____|_| \_\
""")

x = input('How many devices ?: ')


time.sleep(5)

for i in range(int(x)):
    print(i+1)
    pyautogui.click('001.png')
    keyboard.type(fake.bothify(text="????????????????????????"))
    pyautogui.press('tab')
    if i == 0:
        pyautogui.press('enter')
    else:
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)
 
print( """
 _____ ___ _   _ 
|  ___|_ _| \ | |
| |_   | ||  \| |
|  _|  | || |\  |
|_|   |___|_| \_|
                 
""")
