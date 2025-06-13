from dotenv import load_dotenv
import os
import supabase
import platform

load_dotenv()
#env data
sburl = os.getenv('URL')
sbkey = os.getenv('Key')


# Global Viables
supabase = supabase.create_client(sburl, sbkey)
operaingsystem = platform.system()
size = os.get_terminal_size().columns

def clear():
    if operaingsystem == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def pruefe_gerade_ungerade(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False

def style(text):
    lenth_text = len(text)
    if pruefe_gerade_ungerade(size - int(lenth_text)) == False:
        print_gleich = size - lenth_text
        print_gleich = print_gleich / 2
        for i in range(print_gleich):
            print("=", end="")
        print(text)
        for i in range(print_gleich):
            print("=", end="")
    else:
        print_gleich = size - lenth_text - 1
        print_gleich = print_gleich / 2
        for i in range(int(print_gleich)):
            print("=", end="")
        print(text)
        for i in range(int(print_gleich)+1):
            print("=", end="")

        

#def auth():
#
#    credits_response = supabase.auth.sign_in_with_password(
#    {
#        "email": mail,
#        "password": password,
#    }
#)

def main():
    style("Willkommen")

main()

