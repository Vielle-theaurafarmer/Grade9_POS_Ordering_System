
"""Product menu and ordering functions for the POS system."""

import json


MENU = [
    {"id": 1, "name": "Burger", "price": 50.00},
    {"id": 2, "name": "Fries", "price": 35.00},
    {"id": 3, "name": "Soft Drink", "price": 25.00},
]


def display_menu():
    print("\nPRODUCT MENU")
    print("-" * 28)
    for product in MENU:
        print(f"{product['id']}. {product['name']} - P{product['price']:.2f}")
    print("4. Finish order")


def calculate_subtotal(price, quantity):
    return round(price * quantity, 2)


def collect_order():
    order = []

    while True:
        display_menu()
        choice = input("Select a product (1-4): ").strip()

        if choice == "4":
            break

        try:
            product_id = int(choice)
        except ValueError:
            print("Please enter a valid number.")
            continue

        product = next(
            (item for item in MENU if item["id"] == product_id),
            None,
        )
        if product is None:
            print("Invalid product selection.")
            continue

        while True:
            try:
                quantity = int(input(f"Quantity of {product['name']}: ").strip())
                if quantity <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a whole number greater than zero.")

        subtotal = calculate_subtotal(product["price"], quantity)
        existing = next(
            (item for item in order if item["id"] == product["id"]),
            None,
        )
        if existing:
            existing["quantity"] += quantity
            existing["subtotal"] = calculate_subtotal(
                existing["price"], existing["quantity"]
            )
        else:
            order.append(
                {
                    "id": product["id"],
                    "name": product["name"],
                    "price": product["price"],
                    "quantity": quantity,
                    "subtotal": subtotal,
                }
            )

        print(f"Added {quantity} x {product['name']} to the order.")

    return order


def save_order(order, filename="order.json"):
    with open(filename, "w", encoding="utf-8") as output_file:
        json.dump(order, output_file, indent=2)
    print(f"Order saved to {filename}.")


def main():
    order = collect_order()
    if order:
        save_order(order)
    else:
        print("No items were ordered.")


if __name__ == "__main__":
    main()
