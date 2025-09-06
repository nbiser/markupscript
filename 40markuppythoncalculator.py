# price_markup.py

def apply_markup(price, markup_percent):
    return price * (1 + markup_percent / 100)

def main():
    try:
        user_input = input("Enter the base price: $")
        base_price = float(user_input)
        marked_up_price = apply_markup(base_price, 40)
        print(f"Price after 40% markup: ${marked_up_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
