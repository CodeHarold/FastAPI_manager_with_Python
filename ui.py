import helpers
import database as db
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING


class CenterWidgetMixin:
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int((ws / 2) - (w / 2))
        y = int((hs / 2) - (h / 2))
        self.geometry(f"{w}x{h}+{x}+{y}")

class createCustomerWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Create Customer")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=20)

        Label(frame, text="ID 2 ints and 1 upper char").grid(row=0, column=0)
        Label(frame, text="Name from 2 to 30 char").grid(row=1, column=1)
        Label(frame, text="Last Name from 2 to 30 char").grid(row=2, column=2)

        id = Entry(frame)
        id.grid(row=1, column=0)
        id.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        name = Entry(frame)
        name.grid(row=1, column=1)
        name.bind("<KeyRelease>", lambda event: self.validate(event, 1))
        last_name = Entry(frame)    
        last_name.grid(row=1, column=2)
        last_name.bind("<KeyRelease>", lambda event : self.validate(event, 2))

        frame = Frame(self)
        frame.pack(pady=10) 

        create_button = Button(frame, text="Create", command=self.create_customer)
        create_button.configure(state=DISABLED)
        create_button.grid(row=0, column=0)
        Button(frame, text="Cancel", command=self.close).grid(row=0, column=1)


        self.validacion = [0,0,0]
        self.create_button = create_button
        self.id = id
        self.name = name
        self.last_name = last_name

     
    def create_customer(self):
        self.master.treeview.insert(
            parent='', index='end', iid=self.id.get(), 
            values=(self.id.get(), self.name.get(), self.last_name.get()))
        db.Customers.add(self.id.get(), self.name.get(), self.last_name.get())
        self.close()
        
        

    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        value = event.widget.get()
    #     if index == 0:
    #         valided = helpers.validate_id(value, db.Customers.list)
    #         if valided:
    #             event.widget.configure({"bg":"Green"})
    #         else:
    #             event.widget.configure({"bg":"Red"})

    #     if index == 1:
    #         valided = value.isalpha() and len(value) >= 2 and len(value) <= 30
    #         if valided:
    #             event.widget.configure({"bg":"Green"})          
    #         else:
    #             event.widget.configure({"bg":"Red"})

    #     if index == 2:  
    #         valided = value.isalpha() and len(value) >= 2 and len(value) <= 30
    #         if valided:
    #             event.widget.configure({"bg":"Green"})          
    #         else:
    #             event.widget.configure({"bg":"Red"})    

        validate = helpers.validate_id(value, db.Customers.list) if index == 0 \
            else (value.isalpha() and len(value) >= 2 and len(value) <= 30)
        event.widget.configure({"bg": "Green" if validate else "Red"})
        # change the value of self.validacion[index] based on the validation result
        self.validacion[index] = validate
        self.create_button.config(state=NORMAL if self.validacion == [1,1,1] else DISABLED)

        
class EditCustomerWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Edit Customer")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=20)

        Label(frame, text="Unchangeable").grid(row=0, column=0)
        Label(frame, text="Name from 2 to 30 char").grid(row=0, column=1)
        Label(frame, text="Last Name from 2 to 30 char").grid(row=0, column=2)

        id = Entry(frame)
        id.grid(row=1, column=0)
        name = Entry(frame)
        name.grid(row=1, column=1)
        name.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        last_name = Entry(frame)    
        last_name.grid(row=1, column=2)
        last_name.bind("<KeyRelease>", lambda event : self.validate(event, 1))

        customer = self.master.treeview.focus()
        campos = self.master.treeview.item(customer, 'values')
        id.insert(0, campos[0])
        id.configure(state=DISABLED)
        name.insert(0, campos[1])
        last_name.insert(0, campos[2])

        frame = Frame(self)
        frame.pack(pady=10) 

        edit = Button(frame, text="Create", command=self.edit_customer)
        edit.grid(row=0, column=0)
        Button(frame, text="Cancel", command=self.close).grid(row=0, column=1)


        self.validacion = [1,1]
        self.edit = edit
        self.id = id
        self.name = name
        self.last_name = last_name


    def edit_customer(self):
        customer = self.master.treeview.focus()
        self.master.treeview.item(customer, values = (self.id.get(), self.name.get(), self.last_name.get()))
        db.Customers.remove(self.id.get(), self.name.get(), self.last_name.get())
        self.close()
        
    def close(self):
        self.destroy()
        self.update()

        
    def validate(self, event, index):
        value = event.widget.get()
        validate = (value.isalpha() and len(value) >= 2 and len(value) <= 30)
        event.widget.configure({"bg": "Green" if validate else "Red"})
        # change the value of self.validacion[index] based on the validation result
        self.validacion[index] = validate
        self.edit.config(state=NORMAL if self.validacion == [1,1] else DISABLED)



class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title("Customer Management System")
        self.build()
        self.center()
        

    def build(self):
        frame = Frame(self)
        frame.pack()

        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('ID', 'Name', 'Last Name')
        treeview.pack()

        treeview.column('#0', width=0, stretch=NO)
        treeview.column('ID', anchor=CENTER)
        treeview.column('Name', anchor=CENTER)

        treeview.heading('ID', text='ID', anchor=CENTER)
        treeview.heading('Name', text='Name', anchor=CENTER)
        treeview.heading('Last Name', text='Last Name', anchor=CENTER)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        treeview['yscrollcommand'] = scrollbar.set  

        for customer in db.Customers.list:
            treeview.insert(
                parent='', index='end', iid=customer.id, 
                values=(customer.id, customer.name, customer.last_name))
        
        treeview.pack()

        frame = Frame(self)
        frame.pack(pady=20)
    
        Button(frame, text="Add", command=self.create).grid(row=0, column=0)
        Button(frame, text="Remove", command=self.edit).grid(row=0, column=1)
        Button(frame, text="Delete", command=self.delete).grid(row=0, column=2)       


        self.treeview = treeview 

    def delete(self):
        customer = self.treeview.focus()
        if customer:
            campos = self.treeview.item(customer, 'values')
            confirm = askokcancel(title="Delete", message=f"Are you sure you want to delete {campos[1]} {campos[2]}?",
            icon = WARNING)

            if confirm:
                self.treeview.delete(customer)
                db.Customers.delete(campos[0])
            

    def create(self):
        createCustomerWindow(self)

    def edit(self):
        if self.treeview.focus():
            EditCustomerWindow(self)
        
    

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
