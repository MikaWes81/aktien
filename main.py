from dotenv import load_dotenv
import os
import supabase
import platform


load_dotenv()
#env data
sburl = os.getenv('URL')
sbkey = os.getenv('Key')
debugv = os.getenv('DEBUG')


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
        left_padding: int = padding_length // 2
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
    tabellenname = "transaction"
    if debugv == 1:
        print(userid)
    try:
        empf_response = supabase.table(tabellenname).select("amount").eq("userid_empf", userid).execute()
        send_response = supabase.table(tabellenname).select("amount").eq("userid_send", userid).execute()
        # Überprüfen, ob Daten vorhanden sind
        if send_response.data:
            send_amounts = [item["amount"] for item in send_response.data if "amount" in item and isinstance(item["amount"], (int, float))]
        else:
            if debugv == 1:
                print(f"Keine Daten für User-ID '{userid}' in Tabelle '{tabellenname}' gefunden.")
            return 0.0
        if send_response.data:
            empf_amounts = [item["amount"] for item in empf_response.data if "amount" in item and isinstance(item["amount"], (int, float))]

        else:
            if debugv == 1:
                print(f"Keine Daten für User-ID '{userid}' in Tabelle '{tabellenname}' gefunden.")
            return 0.0
        total_amount = sum(empf_amounts) - sum(send_amounts)
        return total_amount

    except Exception as e:
        print(f"Fail to load Data")
        if debugv == 1:
            print(e)
        return 0.0
def auth():
    global credits_response
    global userid
    style("Welcome")
    print("[1] Login")
    print("[2] Exit")
    inp = input()
    if inp == "1":
        try:
            clear()
            style("Login")
            headmail = input("Username: ")
            mail = "projektaktien+" + headmail.strip().lower() + "@gmail.com"
            password = input("Password: ").strip()
            credits_response = supabase.auth.sign_in_with_password({
                "email": mail,
                "password": password,

            })
            userid = credits_response.user.id

            return 1
        except Exception as e:
            print(f"Fail to Login")
            if debugv ==1:
                print(e)
    else:
        return 0

def view_balance():
    style("Balance")
    print("Your Balance: " + str(fetch_amount()) + "€")
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
    clear()
    if auth() ==1:
        clear()
        main_menu()
    else:
        clear()
        return
main()

