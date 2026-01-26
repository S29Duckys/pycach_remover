import os
import ctypes
import time

# Function for clear the console
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Function to check for admin privileges
def is_admin():
    try: 
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Verify admin privileges
def verify_admin():
        if is_admin():
            print("Running with admin privileges. Waiting for 2 seconds...")
            time.sleep(2)
            main()
        else:
            print("you must run this script in admin mode")

# Main menu
def main():
    clear()
    print("Welcome to the PyCache Remove Tool")

if __name__ == "__main__":    
    verify_admin()