from dotenv import load_dotenv
import os
import supabase
import platform
import json

load_dotenv()
#env data
sburl = os.getenv('URL')
sbkey = os.getenv('Key')


# Global Viables
supabase = supabase.create_client(sburl, sbkey)
operaingsystem = platform.system()
credits_response = None


def style(word):
    terminal_width = os.get_terminal_size().columns

    effective_width_for_content = terminal_width - 4

    if len(word) >= effective_width_for_content:
        if len(word) > effective_width_for_content:
            word = word[:effective_width_for_content - 3] + "..."
        padding_length = effective_width_for_content - len(word)
        left_padding = padding_length // 2
        right_padding = padding_length - left_padding

        centered_string_content = "=" * left_padding + word + "=" * right_padding
        final_string = "<" + centered_string_content + ">"
        print(final_string)
        return

    padding_length = effective_width_for_content - len(word)
    left_padding = padding_length // 2
    right_padding = padding_length - left_padding

    centered_string_content = "=" * left_padding + word + "=" * right_padding
    final_string = "<" + centered_string_content + ">"
    print(final_string)


def clear():
    if operaingsystem == "Windows":
        os.system("cls")
    else:
        os.system("clear")



def auth():
    style("Welcome")
    print("[1] Login")
    print("[2] Exit")
    inp = input()
    if inp == "1":
        clear()
        style("Login")
        headmail = input("Username: ")
        mail = headmail.strip().lower() + ".projektaktien@gmail.com"
        password = input("Password: ").strip()
        credits_response = supabase.auth.sign_in_with_password({
            "email": mail,
            "password": password,
        })
        return
    else:
        return



def main():
    auth()

main()

