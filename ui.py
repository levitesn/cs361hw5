from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from users import login, create_user
from features import default_landing_page

console = Console()

def display_main_menu():
    console.clear()
    console.print(Panel("[bold magenta]Welcome to the Inclusive Trip Planner[/bold magenta]", title="Main Menu", border_style="green"))
    console.print("[cyan]1.[/cyan] [green]Login[/green] - Access your saved trips and personalized features")
    console.print("[cyan]2.[/cyan] [green]Create Account[/green] - Join to save and manage trips")
    console.print("[cyan]3.[/cyan] [red]Exit[/red] - Exit the application")

def handle_user_choice():
    choice = Prompt.ask("\nSelect an option", choices=["1", "2", "3"])
    if choice == '1':
        login_page()
    elif choice == '2':
        create_account()
    elif choice == '3':
        console.print("\n[bold red]Exiting the application. Goodbye![/bold red]")
        return False
    return True

def login_page():
    message = ""
    while True:
        console.clear()
        console.print(Panel("[bold magenta]--- Login Page ---[/bold magenta]", border_style="blue"))
        console.print(message)
        username = Prompt.ask("Username")
        password = Prompt.ask("Password", password=True)
        status = login(username, password)
        if status == 0:
            message = "[bold red]Invalid username. Please try again.[/bold red]"
        elif status == 1:
            message = "[bold red]Incorrect password. Please try again.[/bold red]"
        else:
            console.print(f"[bold green]Welcome, {username}![/bold green] You can now access your saved trips and other features.")
            default_landing_page()
            break

def create_account():
    console.clear()
    console.print(Panel("[bold magenta]--- Create Account ---[/bold magenta]", border_style="blue"))
    console.print("[italic]Create an account to start saving your favorite trips and access personalized features.[/italic]")
    username = Prompt.ask("Choose a username")
    password = Prompt.ask("Choose a password", password=True)
    create_user(username, password)
    console.print("[bold green]Account created successfully![/bold green] You can now log in to access all features.")
