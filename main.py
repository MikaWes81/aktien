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

def style(word):
    terminal_width = os.get_terminal_size().columns

    if len(word) >= terminal_width:
        print(word)
        return

    padding_length = terminal_width - len(word)
    left_padding = padding_length // 2
    right_padding = padding_length - left_padding

    centered_string = "=" * left_padding + word + "=" * right_padding
    print(centered_string)

        

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

