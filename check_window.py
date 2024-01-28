from common_window import BaseSubWindow
import tkinter as tk
from tkinter import messagebox
from db_api import Check, Product
from db_api import Session, engine
from sqlalchemy import select

class CheckWindow(BaseSubWindow):

    def __init__(self, parent):
        super().__init__(parent, "Створити чек")
    
    def setup_window(self):
        self.fill_product_list()
        self.selected = list()
        self.total_amount = 0

    def fetch_products(self):
        with Session(engine) as session:
            resultProducts = session.execute(select(Product))
            # product2 = session.execute(select())

            return resultProducts.scalars().all()
        
    def submit_check(self):
        if not self.total_amount is None and not self.total_amount == 0:
            with Session(engine) as session:
                check = Check(amount = self.total_amount,
                            items = self.selected,
                            )
                session.add(check)
                session.commit()
                self.destroy_window()
                messagebox.showinfo("Успіх", "Чек створено")
        else:
            messagebox.showerror("Помилка", "Чек не може бути пустим")

    def fill_product_list(self):
        self.l = self.fetch_products()
        for i in range(len(self.l)):
            self.products.insert(i, self.l[i].title)

        
    def setup_layout(self):
        self.products.grid(row = 0, column = 1, rowspan = 2)
        self.labelProduct.grid(row = 0, column = 0)
        self.labelAmount.grid(row = 2, column = 0)
        self.amountLabel.grid(row = 2, column = 1)
        self.button_submit_check.grid(row = 4, column = 1)
        self.selected_product.grid(row = 0, column = 2, rowspan = 2)
        self.button_add_ptoduct_to_cart.grid(row = 1, column = 0)
        self.button_remove_from_cart.grid(row = 3, column = 2)
        
    def create_ui(self):
        self.products = tk.Listbox(self.root)
        self.labelProduct = tk.Label(self.root, text = "Виберіть товар")
        self.labelAmount = tk.Label(self.root, text = "Сума чека")
        self.amountLabel = tk.Label(self.root, text = "0", bg = "White") 
        self.button_submit_check = tk.Button(self.root, text = "Створити", command = self.submit_check)
        self.selected_product = tk.Listbox(self.root)
        self.button_add_ptoduct_to_cart = tk.Button(self.root, text = "Додати продукт", command = self.add_product_to_cart)
        self.button_remove_from_cart = tk.Button(self.root, text = "Видалити продукт", command = self.remove_from_cart)

    def add_product_to_cart(self):
        l = self.products.curselection()
        for i in l:
            self.selected.append(self.l[i])
        self.apdate_cart_view()

    def remove_from_cart(self):
        for i in self.selected_product.curselection():
            del self.selected[i]
        self.apdate_cart_view()
    
    def apdate_cart_view(self):
        self.total_amount = 0
        self.selected_product.delete(0, tk.END)
        for i in range(len(self.selected)):
            self.selected_product.insert(i, self.selected[i].title)
            self.total_amount += self.selected[i].price
        self.amountLabel["text"] = self.total_amount