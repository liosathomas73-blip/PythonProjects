income_log = []  # List to store daily income


def add_income(amount):
    global balance, savings
    balance += amount  # Add to balance
    income_log.append(amount)  # Log the income
    # Automatically save 10% of each income
    save_amount = amount * 0.1
    savings += save_amount
    balance -= save_amount
    print(f"Income added: ${amount:.2f}")
    print(f"Saved automatically: ${save_amount:.2f}")
    print(f"Current balance: ${balance:.2f}, Total savings: ${savings:.2f}\n")


def view_summary():
    print("------IncomeMate Summary------")
    print(f"Total balance: ${balance:.2f}")
    print(f"Total savings: ${savings:.2f}")
    print(f"Income entries: {income_log}")
    print("------------------------------\n")


def main():
    print("Welcome to IncomeMate!")
    while True:
        print("Choose an option:")
        print("1. Add Income")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            try:
                amount = float(input("Enter income amount: $"))
                add_income(amount)
            except ValueError:
                print("Please enter a valid number.\n")
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Thank you for using IncomeMate. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")
if __name__ == "__main__":
    main()