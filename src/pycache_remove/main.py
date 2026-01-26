import ctypes


def is_admin():
    try: 
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False



# Main menu
def main():
    if is_admin():
        print("Running with admin privileges.")
    else:
        print("you must run this script in admin mode")

if __name__ == "__main__":    
    main()