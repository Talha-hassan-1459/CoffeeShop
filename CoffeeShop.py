def show_menu():
    print("\n--- Coffee Menu ---")
    print("1. Espresso - PKR 750")
    print("2. Latte - PKR 950")
    print("3. Cappuccino - PKR 900")
    print("4. Americano - PKR 700")
    print("5. View Order")
    print("6. Checkout")
    print("7. Exit Customer")
    print("8. View All Receipts Today")
    print("9. Search Receipt by Name")


def coffee_shop(all_bills):

    print("\n☕ Welcome to Coffee Shop!")
    name = input("May I have your name please? ")

    order = []
    total = 0

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            order.append(("Espresso", 750))
            total += 750
            print("Espresso added.")

        elif choice == "2":
            order.append(("Latte", 950))
            total += 950
            print("Latte added.")

        elif choice == "3":
            order.append(("Cappuccino", 900))
            total += 900
            print("Cappuccino added.")

        elif choice == "4":
            order.append(("Americano", 700))
            total += 700
            print("Americano added.")

        elif choice == "5":
            if not order:
                print("Your order is empty.")
            else:
                print("\nYour Order:")
                for item, price in order:
                    print(f"- {item} : PKR {price}")
                print(f"Total so far: PKR {total}")

        elif choice == "6":
            if not order:
                print("No items to checkout.")
            else:
                print("\n--- Final Bill ---")
                for item, price in order:
                    print(f"- {item} : PKR {price}")
                print(f"Total Bill: PKR {total}")

                # store full receipt
                all_bills.append({
                    "name": name,
                    "items": order.copy(),
                    "total": total
                })

                print("✅ Receipt stored.")
            break

        elif choice == "7":
            print("Customer session ended.")
            break

        elif choice == "8":
            print("\n📊 All Receipts Today:")
            if not all_bills:
                print("No receipts yet.")
            else:
                for bill in all_bills:
                    print(f"\nCustomer: {bill['name']}")
                    for item, price in bill["items"]:
                        print(f"- {item} : PKR {price}")
                    print(f"Total: PKR {bill['total']}")

        elif choice == "9":
            search_name = input("Enter customer name to search: ")
            found = False
            for bill in all_bills:
                if bill["name"].lower() == search_name.lower():
                    print(f"\nReceipt for {bill['name']}:")
                    for item, price in bill["items"]:
                        print(f"- {item} : PKR {price}")
                    print(f"Total: PKR {bill['total']}")
                    found = True
            if not found:
                print("No receipt found.")

        else:
            print("Invalid option.")


def main():
    all_bills = []

    while True:
        coffee_shop(all_bills)

        again = input("\nServe next customer? (yes/no): ").lower()
        if again != "yes":
            break

    print("\nSystem closed.")


if __name__ == "__main__":
    main()
