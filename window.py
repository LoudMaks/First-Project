from common_window import BaseWindow
import tkinter as tk
from product_window import ProductWindow
from check_window import CheckWindow
from plot_window import PlotsWindow

class Window(BaseWindow):

    root = tk.Tk()

    def __init__(self):
        super().__init__()
        self.create_ui()
        self.setup_layout()
        self.root.resizable(width = False, height = False)
        self.root.mainloop()

    def create_ui(self):
        self.button_open_create_product_dialog = tk.Button(self.root, text = "Створити вікно створення продукту", command = self.open_product_window)
        self.button_open_create_check_dialog = tk.Button(self.root, text = "Створити вікно створення чеку", command = self.open_check_window)
        self.button_open_plots = tk.Button(self.root, text = "Відкрити вікно графіків", command = self.open_plot_window)

    def setup_layout(self):
        self.button_open_create_product_dialog.grid(row = 0, column = 0)
        self.button_open_create_check_dialog.grid(row = 0, column = 1)
        self.button_open_plots.grid(row = 1, column = 0)

    def open_plot_window(self):
        pl = PlotsWindow(self.root)

    def open_product_window(self):
        pw = ProductWindow(self.root)

    def open_check_window(self):
        ch = CheckWindow(self.root)