import tkinter as tk
win = tk.Tk()

win.geometry(f"500x500+500+100") #габариты и отступы от краев экрана сответственно
win.title('Расчетная программа')
win['bg'] = '#3A1ADB'  #задаем цвет фона

input_weight = tk.Entry(win)
input_weight.grid(row = 2, column = 1)



win.mainloop()