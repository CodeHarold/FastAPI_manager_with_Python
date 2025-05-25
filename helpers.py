
import re
import os
import platform

def clear_screen(): 
    """Clears the console screen based on the operating system."""
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def read_text(length_min=0, length_max=100, message= None):
    print(message) if message else None
    """Reads a line of text from the user with a specified length range."""
    while True:
        text = input(">  ")
        if len(text) >= length_min and len(text) <= length_max:
            return text
      


def validate_id(id, list):
   if not re.match('[0-9]{2}[A-Z]$', id):
       print("Invalid ID format. Must be 2 digits followed by 1 uppercase letter.")
       return False
   for customer in list:
        if customer.id == id:
            print("ID already exists.")
            return False
   return True



