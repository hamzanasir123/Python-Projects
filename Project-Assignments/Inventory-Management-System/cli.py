from inventory import Inventory
from subClass import Electronics, Grocery, Clothing
from exceptions import *
import sys

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Sell Product")
        print("3. Restock Product")
        print("4. Search Product")
        print("5. View All Products")
        print("6. Total Inventory Value")
        print("7. Remove Expired Products")
        print("8. Save Inventory")
        print("9. Load Inventory")
        print("0. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == '1':
                ptype = input("Product Type (Electronics/Grocery/Clothing): ").strip().capitalize()
                pid = input("Product ID: ")
                name = input("Name: ")
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))

                if ptype == 'Electronics':
                    warranty = int(input("Warranty Years: "))
                    brand = input("Brand: ")
                    product = Electronics(pid, name, price, quantity, warranty, brand)

                elif ptype == 'Grocery':
                    expiry = input("Expiry Date (YYYY-MM-DD): ")
                    product = Grocery(pid, name, price, quantity, expiry)

                elif ptype == 'Clothing':
                    size = input("Size: ")
                    material = input("Material: ")
                    product = Clothing(pid, name, price, quantity, size, material)
                else:
                    print("Unknown product type.")
                    continue

                inventory.add_product(product)
                print("Product added.")

            elif choice == '2':
                pid = input("Product ID: ")
                qty = int(input("Quantity to sell: "))
                inventory.sell_product(pid, qty)
                print("Product sold.")

            elif choice == '3':
                pid = input("Product ID: ")
                qty = int(input("Quantity to restock: "))
                inventory.restock_product(pid, qty)
                print("Product restocked.")

            elif choice == '4':
                keyword = input("Search by Name or Type: ")
                if keyword.lower() in ["electronics", "grocery", "clothing"]:
                    results = inventory.search_by_type(keyword)
                else:
                    results = inventory.search_by_name(keyword)
                for p in results:
                    print(p)

            elif choice == '5':
                for p in inventory.list_all_products():
                    print(p)

            elif choice == '6':
                print(f"Total Inventory Value: ${inventory.total_inventory_value():.2f}")

            elif choice == '7':
                inventory.remove_expired_products()
                print("Expired groceries removed.")

            elif choice == '8':
                filename = input("Filename to save: ")
                inventory.save_to_file(filename)
                print("Inventory saved.")

            elif choice == '9':
                filename = input("Filename to load: ")
                inventory.load_from_file(filename)
                print("Inventory loaded.")

            elif choice == '0':
                print("Exiting system.")
                sys.exit()

            else:
                print("Invalid choice.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
