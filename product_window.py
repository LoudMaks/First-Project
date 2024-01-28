from common_window import BaseSubWindow, BaseWindow
import tkinter as tk
from tkinter import messagebox
from db_api import Product, Check
from db_api import Session, engine

class ProductWindow(BaseSubWindow):

    def __init__(self, parent):
        super().__init__(parent, "Додати товар")
        
    def create_ui(self):
        self.titleui = tk.Entry(self.root)
        self.priceui = tk.Entry(self.root)
        self.barcodeui = tk.Entry(self.root)
        self.countui = tk.Entry(self.root)
        self.guarantee = tk.Entry(self.root)
        self.submit = tk.Button(self.root, text = "Підтвердити", command = self.submit_product)
        self.labelTitle = tk.Label(self.root, text = "Назва")
        self.labelPrice = tk.Label(self.root, text = "Ціна")
        self.labelBarcode = tk.Label(self.root, text = "Штрих код")
        self.labelCount = tk.Label(self.root, text = "Кількість")
        self.labelGuarantee = tk.Label(self.root, text = "Гарантія")

    def setup_layout(self):
        self.labelTitle.grid(row = 0, column = 0)
        self.titleui.grid(row = 0, column = 1)
        self.labelPrice.grid(row = 1, column = 0)
        self.priceui.grid(row = 1, column = 1)
        self.labelBarcode.grid(row = 2, column = 0)
        self.barcodeui.grid(row = 2, column = 1)
        self.labelCount.grid(row = 3, column = 0)
        self.countui.grid(row = 3, column = 1)
        self.labelGuarantee.grid(row = 4, column = 0)
        self.guarantee.grid(row = 4, column = 1)
        self.submit.grid(row = 5, column = 0)

    def submit_product(self):
        count = 0
        price = 0
        guarantee = 0
        try:
            count = int(self.countui.get())
            price = float(self.priceui.get())
            guarantee = int(self.guarantee.get())
            if count < 1 or price < 1 or guarantee < 1:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Помилка", " Кількість, ціна та гарантія мають бути цілим числом")
            return
        if self.barcodeui.get() == " ":
            messagebox.showerror("Помилка", "Штрих код не може бути пустим")
            return
        if self.titleui.get() == " ":
            messagebox.showerror("Помилка", "Назва не може бути пустою")
            return
        product = Product(title = self.titleui.get(),
                          price = price,
                          barcode = self.barcodeui.get(),
                          count = count,
                          guarantee = guarantee
                          )
        with Session(engine) as session:
            session.add(product)
            session.commit()
            self.root.destroy()
            messagebox.showinfo("Успіх", "Товар додано")