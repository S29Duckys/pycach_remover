import os
import time
import shutil
import ctypes


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
            print("You must run this script in admin mode")

def remove_pycache_dirs(target_path):
    if not os.path.isdir(target_path):
        print("The provided path is not a valid directory.")
        return
    for current_path, dirs, files in os.walk(target_path):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(current_path, "__pycache__")
            try: 
                shutil.rmtree(pycache_path)
                print(f"Supprimé : {pycache_path}")
            except Exception as e:
                print(f"Erreur avec {pycache_path} : {e}")

# Main menu
def main():
    clear()
    print("Welcome to the PyCache Remove Tool \n")
    path = input("Enter the directory path to remove __pycache__ folders from: ")

    remove_pycache_dirs(path)

if __name__ == "__main__":    
    verify_admin()