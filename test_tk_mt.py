from tkinter import *
import csv
from time import strftime 
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

def open_st():
   # index = np.arange(10) 
   data_frame = pd.read_csv('data.csv', encoding='UTF-8')
   
   
   df = pd.DataFrame(data_frame)
   df.plot(marker='o', markersize=5, grid=1)
   plt.title('Давление и пульс')
   plt.xlabel('Ось Х')
   plt.ylabel('Ось Y')
   # plt.grid(True, color = "grey", linewidth = "1", linestyle = "-.")
   plt.show()

def clear():
   w_dav.delete(0, END)   # удаление введенного текста
   n_dav.delete(0, END)
   puls.delete(0, END)

   
def davlenie():
   current_time1 = strftime("%d-%m")
   wd = (w_dav.get())
   nd = (n_dav.get())
   ps = (puls.get()) 

   with open("data.csv", mode="a", encoding='utf-8') as w_file:
      file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    
    # file_writer.writerow(["1", "2", "3", "4", "5"])
      file_writer.writerow([current_time1, wd, nd, ps])
 
window = Tk()
window.title('Запись давления')
window.geometry('400x300')
 
 
frame = Frame(
   window,
   padx=10,
   pady=10
)
frame.pack(expand=True)
 
 
w_dav = Label(
   frame,
   text="Введите верхнее давление  "
)
w_dav.grid(row=3, column=1)
 
n_dav = Label(
   frame,
   text="Введите нижнее давление  ",
)
n_dav.grid(row=4, column=1)

puls = Label(
   frame,
   text="Введите пульс  ",
)
puls.grid(row=5, column=1)
 
w_dav = Entry(
   frame,
)
w_dav.grid(row=3, column=2, pady=5)
 
n_dav = Entry(
   frame,
)
n_dav.grid(row=4, column=2, pady=5)
puls = Entry(
   frame,
)
puls.grid(row=5, column=2, pady=5)
 
cal_btn = Button(
   frame,
   text='Записать',
   command=davlenie
)
cal_btn.grid(row=6, column=2)


clear_btn = Button(
   frame,
   text='Очистить',
   command=clear
)
clear_btn.grid(row=7, column=2)

open_st_gr = Button(
   frame,
   text='Вывести график',
   command=open_st
)
open_st_gr.grid(row=8, column=2)


# clear_button = ttk.Button(text="Clear", command=clear)
# clear_button.pack(side=LEFT, anchor=N, padx=6, pady=6)
 
window.mainloop()