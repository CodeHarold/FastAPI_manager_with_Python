import os
import helpers
import database as db
def main_menu():
    while True:
        helpers.clear_screen()

        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(  "Welcome to the Menu! ")
        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print("[1] Client Management  ")
        print("[2] Search Client      ")
        print("[3] Add Client         ")
        print("[4] Remove Client      ")
        print("[5] Delete Client      ")
        print("[6] Close program      ")
        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")

        option = input("Select an option: ")
        helpers.clear_screen()

        if option == "1":
            print("Customer Management")
            for customer in db.Customers.list:
                print(customer)
            # Call the function to manage clients here  

            
        elif option == "2":
            print("Search Client")
            id = helpers.read_text(3, 3, "ID (2 int and 1 char):").upper()
            customer = db.Customers.search(id)
            if customer:
                print(f"Client found: {customer}")
            else:
                print("Client not found.")
            # Call the function to search for a client here
                

        elif option == "3":
            print("Add Client")

            id = None
            # Loop until a valid ID is entered
            while True:
                id = helpers.read_text(3, 3, "ID (2 int and 1 char):").upper()
                if helpers.validate_id(id, db.Customers.list):
                    break
               

            name = helpers.read_text(2, 30, "Name (2-30 characters):").capitalize()
            last_name = helpers.read_text(2, 30, "Last Name (2-30 characters):").capitalize()
            db.Customers.add(id,name,last_name)
            print("successfully added customer")
            # Call the function to add a client here
                             
        elif option == "4":
            print("Remove Client...\n")
            id = helpers.read_text(3, 3, "ID (2 int and 1 char):").upper()
            customer = db.Customers.search(id)
            if customer:

                name = helpers.read_text (2, 30, f"Name (2-30 characters)[{customer.name}]").capitalize()
                
                last_name = helpers.read_text (2, 30, f"Last Name (2-30 characters)[{customer.last_name}]").capitalize()

                db.Customers.remove(id, name,last_name)
                print("Client successfully removed.")   
            else:
                print("Client not found.")

                
        elif option == "5":
            print("Delete Client...\n")
            id = helpers.read_text(3, 3, "ID (2 int and 1 char):").upper() 
            print( "Client successfully deleted.") if db.Customers.delete(id) else print("Client not found.")

            
               
        elif option == "6":
            print("Closing program...")
            break
        else:
            print("Invalid option. Please try again.")

        input("\nPress Enter to continue...")











     

