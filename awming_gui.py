import tkinter as tk
import gui_func as gui
from tkinter import ttk

class MainFrame(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.dash1()
        self.dash2()
        self.dash3()
        self.buttons(controller)

    def dash1(self):
        dash1Frame = ttk.Frame(self, height=self.winfo_screenheight()/4, width=self.winfo_screenwidth(), relief='groove')
        ttk.Label(dash1Frame, text="HELLO, NAME!", background='#0F52BA', foreground='white', style='dash1Label.TLabel').pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.style = ttk.Style(self)
        self.style.configure('dash1Label.TLabel', font=('Helvetica', 100))
        dash1Frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=0)
        dash1Frame.pack_propagate(False)

    def dash2(self):
        dash2Frame = ttk.Frame(self, height=self.winfo_screenheight()/8, width=self.winfo_screenwidth(), relief='solid')
        dash2Frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=0)
        dash2Frame.pack_propagate(False)
    
    def dash3(self):
        dash3Frame = ttk.Frame(self, height=self.winfo_screenheight()/2, width=self.winfo_screenwidth()/2, relief='solid')
        dash3Frame.pack(side=tk.LEFT, fill=tk.NONE, padx=10, pady=20)
        dash3Frame.pack_propagate(False)
    
    def buttons(self, controller):
        buttons = ttk.Frame(self, height=self.winfo_screenheight()/2, width=self.winfo_screenwidth()/2, relief='solid')
        buttons.grid_columnconfigure(0, weight=1)
        buttons.grid_columnconfigure(1, weight=1)
        buttons.grid_rowconfigure(0, weight=1)
        buttons.grid_rowconfigure(1, weight=1)
        buttons.grid_rowconfigure(2, weight=1)

        sale = ttk.Button(buttons, text="Make a Sale", command=lambda: controller.ShowFrame("Sale"))
        sale.grid(column=0, row=0, sticky=tk.NSEW)
        sale.grid_propagate(False)

        lookup = ttk.Button(buttons, text="Lookup Price")
        lookup.grid(column=1, row=0, sticky=tk.NSEW)
        lookup.grid_propagate(False)

        incoming = ttk.Button(buttons, text="Record Incoming")
        incoming.grid(column=0, row=1, sticky=tk.NSEW)
        incoming.grid_propagate(False)

        void = ttk.Button(buttons, text="Void Transaction")
        void.grid(column=1, row=1, sticky=tk.NSEW)
        void.grid_propagate(False)

        outgoing = ttk.Button(buttons, text="Record Outgoing")
        outgoing.grid(column=0, row=2, sticky=tk.NSEW)
        outgoing.grid_propagate(False)

        calc = ttk.Button(buttons, text="Calculator")
        calc.grid(column=1, row=2, sticky=tk.NSEW)
        calc.grid_propagate(False)
        
        self.style = ttk.Style(self)
        self.style.configure('TButton', font=('Helvetica', 40))

        buttons.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=20)
        buttons.pack_propagate(False)

class SaleFrame(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        salesLists = {}

        barcodeFrame = ttk.Frame(self, height=self.winfo_screenheight()/8, width=self.winfo_screenwidth()/2)

        ttk.Label(barcodeFrame, text="Barcode: ", style="barcodeLabel.TLabel").pack(side=tk.LEFT, padx = 30)
        self.style = ttk.Style(self)
        self.style.configure('barcodeLabel.TLabel', font=('Helvetica', 40))

        barcode = tk.StringVar()
        barcodeEntry = ttk.Entry(barcodeFrame, textvariable=barcode)
        print(barcode.get())
        barcodeEntry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=30, ipadx=40, ipady=10)

        barcodeEntry.focus()
        barcodeEntry.bind('<Return>', lambda x: self.printSalesList(barcode.get(), salesListFrame, salesLists, keep_labels, totalSaleFrame))
        
        barcodeFrame.pack(side=tk.TOP, pady=10)
        barcodeFrame.pack_propagate(False)

        salesListFrame = ttk.Frame(self, height=self.winfo_screenheight()/2, width=1700, relief='solid')

        salesListFrame.grid_columnconfigure(0, weight=2)
        salesListFrame.grid_columnconfigure(1, weight=2)
        salesListFrame.grid_columnconfigure(2, weight=1)
        

        item_name = ttk.Label(salesListFrame, text = "Item Name", width=600, style='salesList.TLabel')
        item_name.grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)
        item_name.grid_propagate(0)

        item_num = ttk.Label(salesListFrame, text = "Number of Items", width=600, style='salesList.TLabel')
        item_num.grid(column=1, row=0, sticky=tk.NSEW, padx=10, pady=10)
        item_num.grid_propagate(0)

        item_price = ttk.Label(salesListFrame, text = "Price", width=300, style='salesList.TLabel')
        item_price.grid(column=2, row=0, sticky=tk.NSEW, padx=10, pady=10)
        item_price.grid_propagate(0)

        keep_labels = [item_name, item_num, item_price]

        self.style.configure('salesList.TLabel', font=('Helvetica', 25))

        salesListFrame.pack(side=tk.TOP, padx = 10, pady=10, anchor=tk.W)
        salesListFrame.pack_propagate(0)

        totalSaleFrame = ttk.Frame(self, height = 50, width = 1700, relief='solid')

        totalSaleFrame.grid_columnconfigure(0, weight=2)
        totalSaleFrame.grid_columnconfigure(1, weight=2)
        totalSaleFrame.grid_columnconfigure(2, weight=1)
        totalSaleFrame.grid_propagate(0)
        
        total = ttk.Label(totalSaleFrame, width=680, text="Total", style='salesList.TLabel')
        total.grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)

        
        totalSaleFrame.pack(side=tk.LEFT, padx = 10, pady=10, anchor=tk.SW)
        totalSaleFrame.pack_propagate(0)

        checkoutFrame = ttk.Frame(self, height=50, width=300, relief='solid')

        checkout = ttk.Button(checkoutFrame, width=300, text="CHECKOUT", style='checkout.TButton', command=lambda: self.showConfirmFrame())
        checkout.pack(padx=10, pady=10)
        self.style.configure('checkout.TButton', font=('Helvetica', 15))

        checkoutFrame.pack(side=tk.RIGHT, padx = 10, pady=10, anchor=tk.SE)
        checkoutFrame.pack_propagate(0)

    def printSalesList(self, barcode, frame, salesLists, keep_labels, totalFrame):
        
        for child in frame.winfo_children():
            if (child not in keep_labels):
                print(child)
                child.destroy()

        salesLists = gui.barcode_lookup(barcode, salesLists)
        
        row_count = 1

        item_count = 0
        total_price = 0

        for keys in salesLists.keys():
            frame.grid_rowconfigure(row_count, weight=1)
            row_count += 1
            
            tuple = salesLists[keys]
            ttk.Label(frame, text = tuple[0], width=680, style='salesList.TLabel').grid(column=0, row=row_count, sticky=tk.NSEW, padx=10, pady=10)
            ttk.Label(frame, text = tuple[1], width=680, style='salesList.TLabel').grid(column=1, row=row_count, sticky=tk.NSEW, padx=10, pady=10)
            ttk.Label(frame, text = tuple[2], width=340, style='salesList.TLabel').grid(column=2, row=row_count, sticky=tk.NSEW, padx=10, pady=10)

            item_count = item_count + tuple[1]
            total_price = total_price + tuple[2]

            ttk.Label(totalFrame, width=680, text = item_count, style='salesList.TLabel').grid(column=1, row=0, sticky=tk.NSEW, padx=10, pady=10)
            ttk.Label(totalFrame, width=340, text = total_price, style='salesList.TLabel').grid(column=2, row=0, sticky=tk.NSEW, padx=10, pady=10)
    
    def showConfirmFrame(self):
        app = confirmFrame()
        app.mainloop()

class confirmFrame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Confirm?")
        self.geometry('200x150+400+300') 
        self.resizable(False, False)
               
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Awming Pet Supplies")
        self.iconphoto(False, tk.PhotoImage(file='app.png'))

        screen_width = str(self.winfo_screenwidth())
        screen_height = str(self.winfo_screenheight())
        self.geometry(screen_width + "x" + screen_height + "+0+0")
        self.resizable(False, False)

        container = tk.Frame(self)
        container.pack()

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        main = MainFrame(container,self)
        sale = SaleFrame(container,self)

        self.frames["Main"]=main
        self.frames["Sale"]=sale

        main.grid(row=0,column=0,sticky="nsew")
        sale.grid(row=0,column=0,sticky="nsew")

        self.ShowFrame("Main")

    def ShowFrame(self, index):
        frame = self.frames[index]
        frame.tkraise()
        
    
if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
