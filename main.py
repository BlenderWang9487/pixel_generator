import tkinter as tk
from functools import partial

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.gr = tk.Frame(master=self)
        self.gr.grid(row=0)
        self.arr = []
        self.pack()
        self.create_widgets(16)

    def create_widgets(self,n):
        for i in range(n):
            l = []
            for j in range(n):
                b = tk.Button(self.gr,width=2,height=1,bg="white")
                b["command"] = partial(self.chbg,b)
                b.grid(row=i,column=j)
                l.append(b)
            self.arr.append(l)
        self.middle = tk.Frame(self)
        self.middle.grid(row=1)
        self.gen1 = tk.Button(self.middle,text="Generate8x8",
                              command=partial(self.generate,8))
        self.gen1.grid(row=0,column=0)
        self.gen2 = tk.Button(self.middle,text="Generate16x16",
                              command=partial(self.generate,16))
        self.gen2.grid(row=0,column=1)
        self.clear = tk.Button(self.middle,text="clear",
                              command=self.clear)
        self.clear.grid(row=0,column=2)
        self.textbox = tk.Text(self,height=10)
        self.textbox.grid(row=2)

    def chbg(self,b):
        b['bg'] = "white" if b['bg'] == "black" else "black"
    
    def generate(self,n):
        s = "{"
        if n == 8:
            for c in range(8):
                sum = 0
                t = 1
                for r in range(8):
                    if self.arr[r][c]['bg'] == "black":
                        sum += t
                    t *= 2
                s += hex(sum) + (',' if c < 7 else '};')
        elif n == 16:
            for c in range(16):
                sum = 0
                t = 1
                for r in range(8):
                    if self.arr[r][c]['bg'] == "black":
                        sum += t
                    t *= 2
                s += hex(sum) + ','
            s += "\n"
            for c in range(16):
                sum = 0
                t = 1
                for r in range(8,16):
                    if self.arr[r][c]['bg'] == "black":
                        sum += t
                    t *= 2
                s += hex(sum) + (',' if c < 15 else '};')
        else:
            assert False, "Wrong number!"
        self.textbox.delete(1.0,'end')
        self.textbox.insert('insert',s)
    
    def clear(self):
        for i in self.arr:
            for j in i:
                j['bg'] = "white"
        self.textbox.delete(1.0,'end')

if __name__=="__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()