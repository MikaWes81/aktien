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
userid = None


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

def fetch_amount():
    TABELLENNAME = "balance"
    try:

        # Daten abrufen: Filtere nach userid und wähle nur die Spalte 'amount' aus
        # Angenommen, die Spalte für die User-ID heißt 'userid'
        response = supabase.table(TABELLENNAME).select("amount").eq("userid", userid).execute()

        # Überprüfen, ob Daten vorhanden sind
        if response.data:
            amounts = [item["amount"] for item in response.data if "amount" in item and isinstance(item["amount"], (int, float))]
            total_amount = sum(amounts)
            return total_amount
        else:
            print(f"Keine Daten für User-ID '{userid}' in Tabelle '{TABELLENNAME}' gefunden.")
            return 0.0

    except Exception as e:
        print(f"Fehler beim Abrufen der Daten: {e}")
        return 0.0

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
        user_id = credits_response.user.id

        return
    else:
        return

def view_balance():
    style("Balance")
    print("Your Balance: " + str(fetch_amount()))
    print("[1] Make an Transaction")
    print("[2] Main Menu")
    inp = input()
    match inp:
        case "2":
            return


def main_menu():
    style("Main Menu")
    print("[1] View Acount Balance")
    print("[2] Make an Tranceaktion")
    print("[3] Start an Buisness")
    print("[4] Editing Buisness")
    print("[5] Buy shares")
    print("[6] Logout")
    inp = input()
    match inp:
        case "1":
            clear()
            view_balance()





def main():
    auth()
    clear()
    main_menu()

main()

