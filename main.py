from ui import display_main_menu, handle_user_choice


def main():
    while True:
        display_main_menu()
        if not handle_user_choice():
            break  # Exit the loop if the user chooses to exit


if __name__ == "__main__":
    main()
