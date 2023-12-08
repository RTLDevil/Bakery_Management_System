def display_inventory():
    try:
        with open("inventory.txt", "r") as file:
            inventory_data = file.readlines()
            items = []
            for line in inventory_data:
                if ':' in line:
                    stock_name, stock_level = line.strip().split(':')
                    items.append(f"{stock_name}: {stock_level}")
            if items:
                print("Inventory:")
                for item in items:
                    print(item)
            else:
                print("Inventory is empty.")
    except FileNotFoundError:
        print("Inventory file not found. Creating a new file.")
        initialize_inventory_file()
        display_inventory()
    except Exception as e:
        print("An error occurred:", str(e))
def initialize_inventory_file():
    with open("inventory.txt", "w") as file:
        file.write("Welcome to the Bakery Inventory System!\n")
def add_item_to_inventory():
    try:
        stock_name = input("Enter the name of the item: ")
        stock_level = int(input("Enter the stock level: "))
        inventory_data = read_inventory_data()
        item_found = False
        with open("inventory.txt", "w") as file:
            for line in inventory_data:
                if ':' in line:
                    item_name, existing_stock_level = line.strip().split(':')
                    if item_name == stock_name:
                        new_stock_level = int(existing_stock_level) + stock_level
                        file.write(f"{stock_name}:{new_stock_level}\n")
                        item_found = True
                    else:
                        file.write(line)
            if not item_found:
                file.write(f"{stock_name}:{stock_level}\n")
        print(f"Item '{stock_name}' added to the inventory with stock level {stock_level}.")
    except ValueError:
        print("Invalid input. Please enter a valid stock level.")
    except Exception as e:
        print("An error occurred:", str(e))
def read_inventory_data():
    try:
        with open("inventory.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print("Inventory file not found. Creating a new file.")
        initialize_inventory_file()
        return []
def prevent_sell():
    try:
        stock_name = input("Enter the name of the item to sell: ")
        quantity_to_sell = int(input(f"Enter the quantity of '{stock_name}' to sell: "))
        if check_stock(stock_name, quantity_to_sell):
            update_inventory(stock_name, -quantity_to_sell)
            print(f"Selling {quantity_to_sell} of '{stock_name}'.")
            print("Inventory updated successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid quantity.")
def check_stock(stock_name, quantity):
    inventory_data = read_inventory_data()
    for line in inventory_data:
        if ':' in line:
            item_name, stock_level = line.strip().split(':')
            if item_name == stock_name:
                if int(stock_level) >= quantity:
                    return True
                else:
                    print(f"Sorry, '{stock_name}' is out of stock.")
                    return False
    print(f"Sorry, '{stock_name}' is not found in the inventory.")
    return False
def update_inventory(stock_name, quantity):
    inventory_data = read_inventory_data()
    with open("inventory.txt", "w") as file:
        for line in inventory_data:
            if ':' in line:
                item_name, stock_level = line.strip().split(':')
                if item_name == stock_name:
                    new_stock_level = int(stock_level) + quantity
                    file.write(f"{stock_name}:{new_stock_level}\n")
                else:
                    file.write(line)
def record_sales():
    try:
        stock_name = input("Enter the name of the item sold: ")
        quantity_sold = float(input(f"Enter the quantity of '{stock_name}' sold: "))
        total_price = float(input(f"Enter the total price for '{stock_name}': "))
        num_sales = get_next_sale_number()
        log_sale(num_sales, stock_name, quantity_sold, total_price)
        print(f"Sale recorded as #{num_sales} for {quantity_sold} of '{stock_name}'.")
        print(f"Total Price: ${total_price:.2f}")
        print("Sales record updated successfully.")
    except ValueError:
        print("Invalid input. Please enter valid quantity and total price.")
def get_next_sale_number():
    try:
        with open("sales.txt", "r") as file:
            sales_data = file.readlines()
            return len(sales_data) + 1
    except FileNotFoundError:
        with open("sales.txt", "w") as file:
            return 1
def log_sale(sale_num, product, quantity, total_price):
    with open("sales.txt", "a") as file:
        file.write(f"{sale_num},{product},{quantity},{total_price}\n")

def display_sales_and_revenue():
    try:
        with open("sales.txt", "r") as file:
            sales_data = file.readlines()
            if not sales_data:
                print("No sales data found.")
                return
            total_revenue = 0
            print("Sales Information:")
            for sale_record in sales_data:
                sale_info = sale_record.strip().split(',')
                sale_num, product, quantity, total_price = sale_info
                quantity = float(quantity)
                total_price = float(total_price)
                total = quantity * total_price
                print(f"Sale #{sale_num}: {quantity} of '{product}' for ${total_price:.2f} each. Total: ${total:.2f}")
                total_revenue += total
            print(f"Total Revenue: ${total_revenue:.2f}")
    except FileNotFoundError:
        print("Sales file 'sales.txt' not found.")
    except IOError as e:
        print(f"Error accessing sales file: {e}")

def main():
    while True:
        ask = input("pick one? (Y or N): ").upper()
        if ask != "Y":
            break
        print("Bakery Management System.")
        print("1: Display_Inventory.")
        print("2: Add New Item.")
        print("3: Make Sells.")
        print("4: Record the Sales.")
        print("5: Display Sales and Revenues.")
        print("6: Exit")
        choice = int(input("Pick one option.: "))
        if choice == 1:
            display_inventory()
        elif choice == 2:
            add_item_to_inventory()
        elif choice == 3:
            prevent_sell()
        elif choice == 4:
            record_sales()
        elif choice == 5:
            display_sales_and_revenue()
# Call the Main function.
main()