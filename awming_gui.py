import tkinter as tk
from tkinter import ttk

class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

    
        dash1 = self.subFrame(self.winfo_screenheight()/4, self.winfo_screenwidth(), 'groove', tk.TOP, tk.X, 10, 0)

        dash2 = self.subFrame(self.winfo_screenheight()/8, self.winfo_screenwidth(), 'solid', tk.TOP, tk.X, 10, 0)

        dash3 = self.subFrame(self.winfo_screenheight()/2, self.winfo_screenwidth()/2, 'solid', tk.LEFT, tk.NONE, 10, 20)
        
        buttons = self.subFrame(self.winfo_screenheight()/2, self.winfo_screenwidth()/2, 'solid', tk.LEFT, tk.NONE, 10, 20)
        
        self.pack(padx=5, pady=5)

    def subFrame(self, h, w, r, s, f, px, py):
        subFrame = ttk.Frame(self, height=h, width=w, relief=r)
        subFrame.pack(side=s, fill=f, padx=px, pady=py)

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Awming Pet Supplies")
        self.iconphoto(False, tk.PhotoImage(file='app.png'))

        screen_width = str(self.winfo_screenwidth())
        screen_height = str(self.winfo_screenheight())
        self.geometry(screen_width + "x" + screen_height + "+0+0")
        self.resizable(False, False)
    
if __name__ == '__main__':
    app = MainWindow()
    MainFrame(app)
    app.mainloop()
