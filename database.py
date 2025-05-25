import csv
import config





class Customer:
    def __init__(self, id, name, last_name):
        self.id = id
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f"({self.id}, {self.name} {self.last_name})"
    
    def to_dict(self):
        return {"id": self.id, "name": self.name, "last_name": self.last_name }
    
class Customers:

    list = []
    with open(config.DATABASE_PATH, newline='\n') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
           if len(row) == 3:  # Ensure the row has exactly 3 columns
                id, name, last_name = row
                customer = Customer(id, name, last_name)
                list.append(customer)
           else:
                print(f"skipping invalied row: {row}")  



    @staticmethod
    def search(id):
        for customer in Customers.list:
            if customer.id == id:
                return customer
        
    @staticmethod
    def add(id, name, last_name):
        customer = Customer(id, name, last_name)
        Customers.list.append(customer)
        Customers.save()
        return customer
    
    
    @staticmethod
    def remove(id,name, last_name):
        for index,customer in enumerate (Customers.list):
            if customer.id == id:
                Customers.list[index].name = name
                Customers.list[index].last_name = last_name
                Customers.save()
                return Customers.list[index]
            
    @staticmethod
    def delete(id):
        for index,customer in enumerate (Customers.list):
            if customer.id == id:
                customer = Customers.list.pop(index)
                Customers.save()
                return customer
         
                

    @staticmethod
    def  save():
        with open(config.DATABASE_PATH, 'w',  newline='\n') as file:
            writer = csv.writer(file, delimiter=';')
            for customer in Customers.list:
                writer.writerow((customer.id, customer.name, customer.last_name))

