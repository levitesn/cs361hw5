from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

EXCHANGE_RATES = {
    'USD': {'EUR': 0.85, 'GBP': 0.75, 'JPY': 110.0},
    'EUR': {'USD': 1.18, 'GBP': 0.88, 'JPY': 129.0},
    'GBP': {'USD': 1.33, 'EUR': 1.14, 'JPY': 147.0},
    'JPY': {'USD': 0.0091, 'EUR': 0.0078, 'GBP': 0.0068}
}

def default_landing_page():
    while True:
        console.clear()
        console.print(Panel("[bold magenta]--- Default Landing Page ---[/bold magenta]", border_style="green"))
        console.print("[cyan]1.[/cyan] [green]View Saved Trips[/green] - Review and manage your saved trips")
        console.print("[cyan]2.[/cyan] [green]Itinerary and Travel Assistance[/green] - Get help planning your travel route")
        console.print("[cyan]3.[/cyan] [green]Currency Conversion[/green] - Convert currencies for your travels")
        console.print("[cyan]4.[/cyan] [red]Logout[/red] - Return to the main menu")
        choice = Prompt.ask("\nSelect an option", choices=["1", "2", "3", "4"])

        if choice == '1':
            view_saved_trips()
        elif choice == '2':
            itinerary_and_travel_assistance()
        elif choice == '3':
            currency_conversion()
        elif choice == '4':
            break

def view_saved_trips():
    console.clear()
    console.print(Panel("[bold magenta]--- Saved Trips ---[/bold magenta]", border_style="blue"))
    trips = ["Trip to Paris", "Trip to Tokyo", "Trip to New York"]
    table = Table(title="Saved Trips")
    table.add_column("Trip Name", style="cyan")
    for trip in trips:
        table.add_row(trip)
    console.print(table)
    console.print("[italic]Select a trip to view details or make changes.[/italic]")
    console.print("\nPress [bold green]Enter[/bold green] to return to the landing page...")
    input()

def itinerary_and_travel_assistance():
    console.clear()
    console.print(Panel("[bold magenta]--- Itinerary and Travel Assistance ---[/bold magenta]", border_style="blue"))
    console.print("[bold yellow]Feature coming soon...[/bold yellow] This will help you plan travel routes and view estimated times between destinations.")
    console.print("\nPress [bold green]Enter[/bold green] to return to the landing page...")
    input()

def currency_conversion():
    console.clear()
    console.print(Panel("[bold magenta]--- Currency Conversion ---[/bold magenta]", border_style="blue"))
    console.print("[italic]Convert currencies to help you budget your trip expenses. Try different amounts and currency pairs.[/italic]")

    amount = Prompt.ask("Enter amount to convert", default="1.0")
    from_currency = Prompt.ask("From currency (e.g., USD)", default="USD").upper()
    to_currency = Prompt.ask("To currency (e.g., EUR)", default="EUR").upper()

    try:
        amount = float(amount)
        converted_amount = convert_currency(amount, from_currency, to_currency)
        console.print(f"[bold green]Converted {amount} {from_currency} to {converted_amount:.2f} {to_currency}[/bold green]")
    except ValueError:
        console.print("[bold red]Invalid amount entered. Please enter a numeric value.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")

    console.print("\nPress [bold green]Enter[/bold green] to return to the landing page...")
    input()

def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount

    if from_currency not in EXCHANGE_RATES or to_currency not in EXCHANGE_RATES[from_currency]:
        raise ValueError("Currency conversion not available for the selected pair.")

    rate = EXCHANGE_RATES[from_currency][to_currency]
    return amount * rate
