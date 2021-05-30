import tkinter as tk;
import math
#Practical
class Application(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.pack()
    self.create_widgets()

  def create_widgets(self):
    self.reset = False
    self.current = 0
    self.result = tk.Label(self, text=f'''{self.current}''')
    self.result.grid(columnspan=5)
    self.numbers = [tk.Button(self) for i in range(0, 10)]
    
    for n in range(0, 10):
      self.numbers[n]["text"] = n

    for i in range(0, 3):
      for j in range(0, 3):
        self.numbers[j + i * 3 + 1].grid(column = j, row = 3 - i)
    self.numbers[0].grid(column = 0, row = 4)

    self.numbers[0]["command"] = (lambda: self.update_current)
    self.numbers[1]["command"] = (lambda: self.update_current(1))
    self.numbers[2]["command"] = (lambda: self.update_current(2))

    self.numbers[3]["command"] = (lambda: self.update_current(3))
    self.numbers[4]["command"] = (lambda: self.update_current(4))
    self.numbers[5]["command"] = (lambda: self.update_current(5))
    self.numbers[6]["command"] = (lambda: self.update_current(6))

    self.numbers[7]["command"] = (lambda: self.update_current(7))
    self.numbers[8]["command"] = (lambda: self.update_current(8))
    self.numbers[9]["command"] = (lambda: self.update_current(9))

    self.add = tk.Button(self)
    self.sub = tk.Button(self)
    self.mul = tk.Button(self)
    self.div = tk.Button(self)
    self.eq = tk.Button(self)

    self.add["text"] = "+"
    self.sub["text"] = "-"
    self.mul["text"] = "*"
    self.div["text"] = "/"
    self.eq["text"] = "="

    self.add["command"] = self.addition
    self.sub["command"] = self.subtraction
    self.mul["command"] = self.multiply
    self.div["command"] = self.division
   
    self.eq["command"] = self.solve
    self.clear = tk.Button(self, text="C", command = self.clear, fg = "red")
    self.dot = tk.Button(self, text=".", command = self.add_decimal)

    self.add.grid(row = 1, column = 4)
    self.sub.grid(row = 2, column = 4)
    self.mul.grid(row = 3, column = 4)
    self.div.grid(row = 4, column = 4)
    self.eq.grid(row=4,  column = 1)
    self.dot.grid(row=4, column = 2)
    self.clear.grid(row=3, column = 5)

    self.pi = tk.Button(self, text=u'''\u03C0''')
    self.e = tk.Button(self, text="e")

    self.pi.grid(row = 1, column = 5)
    self.e.grid(row = 2, column = 5)

    self.pi["command"] = lambda: self.set_current(math.pi)
    self.e["command"] = lambda: self.set_current(math.e)
 #   self.quit = tk.Button(self, text="QUIT", fg="red",                        command=self.master.destroy)
  def add_decimal(self):
    if self.result["text"][-1] == ".":
      self.result["text"] = self.result["text"][0:-1]
    elif "." in self.result["text"]:
      return
    else:
      self.result["text"] += "."

  def update_current(self, value = 0):
    if self.reset == True:
      self.current = value
    elif "." in self.result["text"]:
      if len(self.result["text"]) == 12:
        return
      self.current += (int(value) * (10 ** ( -1 * len(self.result["text"][self.result["text"].find("."):]))))
      print(len(self.result["text"][self.result["text"].find("."):]))
    else:
      self.current = self.current * 10 + int(value)
    self.result["text"] = '''{:8f}'''.format(self.current).rstrip("0").rstrip(".")
  
  def set_current(self, value):
    self.current = value
    self.result["text"] = '''{:8f}'''.format(self.current).rstrip('0').rstrip(".")

  def clear(self):
    if self.current == 0:
      self.stored = 0
    self.current = 0
    self.update_current()
  def addition(self):
    self.chfunc()
    self.func = self.stored.__add__
  def subtraction(self):
    self.chfunc()
    self.func = self.stored.__sub__
  def multiply(self):
    self.chfunc()
    self.func = self.stored.__mul__
  def division(self):
    self.chfunc()
    self.func = self.stored.__truediv__
  def chfunc(self):
    self.stored = self.current
    self.reset = True
    self.current = self.stored
  

  def solve(self):
    try:
      self.current = self.func(self.current)
      self.stored = self.current
    except ZeroDivisionError:
      self.current = 0
    except TypeError:
      self.current = self.stored * self.current
      self.stored = self.current
    finally:
      self.func = None
      self.result["text"] = '''{:8f}'''.format(self.current).rstrip("0").rstrip(".")

if __name__ == '__main__':
  root = tk.Tk()
  app = Application(master=root)
  app.mainloop()