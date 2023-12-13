import psycopg2
conn=psycopg2.connect(dbname="student_107", host="pgdb.uni-dubna.ru", user="student107", password="1234Temp", port="5432")

cursor = conn.cursor()
#cursor.execute("SELECT * FROM exeple")
#print(cursor.fetchall())
#conn.close()

from tkinter import *
import tkinter as tk
from tkinter import ttk



#действие при нажатии на веведения
def clicked():
    if monthchoosen.get() == 'earnings':
        cursor.execute("SELECT * FROM b_earnings")
    if monthchoosen.get() == 'product':
        cursor.execute("SELECT * FROM b_product")
    if monthchoosen.get() == 'store':
        cursor.execute("SELECT * FROM b_shop")
    if monthchoosen.get() == 'seller':
        cursor.execute("SELECT * FROM b_sellers")
    if monthchoosen.get() == 'provider':
        cursor.execute("SELECT * FROM b_provider")
    results = cursor.fetchall()
    root = tk.Tk()
    text = tk.Text(root)
    text.pack()
    for row in results:
        text.insert(tk.END, str(row) + '\n')
    root.mainloop()

    #действие при нажатии на insert
def clickinsert():
    b=entry.get()
    b=b.split()
    if monthchoosen1.get() == 'earnings':
        cursor.execute("INSERT INTO b_earnings  VALUES (%s, %s,%s, %s)",b)
        conn.commit() 
    if monthchoosen1.get() == 'product':
        cursor.execute("INSERT INTO b_product  VALUES (%s, %s,%s)",b)
        conn.commit() 
    if monthchoosen1.get() == 'store':
        cursor.execute("INSERT INTO b_shop VALUES (%s, %s,%s,%s,%s)",b)
        conn.commit() 
    if monthchoosen1.get() == 'seller':
        cursor.execute("INSERT INTO b_sellers  VALUES (%s, %s,%s,%s)",b)
        conn.commit() 
    if monthchoosen1.get() == 'provider':
        cursor.execute("INSERT INTO b_provider  VALUES (%s, %s)",b)
        conn.commit() 
    print("Data add")

#действие при нажатии на delete
def clickdelete():
    b=entry1.get()
    b=b.split()
    if monthchoosen2.get() == 'earnings':
        cursor.execute("DELETE FROM b_earnings WHERE date =%s",b)
        conn.commit() 
    if monthchoosen2.get() == 'product':
        cursor.execute("DELETE FROM b_product WHERE product_id =%s",b)
        conn.commit() 
    if monthchoosen2.get() == 'store':
        cursor.execute("DELETE FROM b_shop WHERE shop_id =%s",b)
        conn.commit() 
    if monthchoosen2.get() == 'seller':
        cursor.execute("DELETE FROM b_sellers  WHERE sellers_id =%s",b)
        conn.commit() 
    if monthchoosen2.get() == 'provider':
        cursor.execute("DELETE FROM  b_provider  WHERE provider_id =%s",b)
        conn.commit() 
    print("Data delete")

def clickf():
    b=entry2.get()
    b=b.split()
    cursor.execute("SELECT proect_f(%s)",b)
    results = cursor.fetchall()
    root = tk.Tk()
    text = tk.Text(root)
    text.pack()
    for row in results:
        text.insert(tk.END, str(row) + '\n')
    root.mainloop()

def clickf2():
    b=entry3.get()
    b=b.split()
    cursor.execute("SELECT proect_f2(%s, %s)",b)
    results = cursor.fetchall()
    root = tk.Tk()
    text = tk.Text(root)
    text.pack()
    for row in results:
        text.insert(tk.END, str(row) + '\n')
    root.mainloop()
window = Tk()
window.title("PythonRu")
window.geometry('400x500')
#кнопка для выведения таблицы
btn = Button(window, text="Show tables", command=clicked)  
#btn.grid(column=1, row=0)
btn.place(x=200, y=50)
#окно ввода
entry = ttk.Entry()
entry.place(x=210, y=120)

#кнопка для вставки в таблицу
btn1 = Button(window, text="Insert", command=clickinsert)  
btn1.place(x=350, y=120)

#combobox
n = tk.StringVar() 
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n) 
  
monthchoosen['values'] = ('earnings',  
                          'product', 
                          'store', 
                          'seller',
                          'provider'
                          ) 
monthchoosen.place(x=10, y=50)
#monthchoosen.grid(column = 1, row = 5) 
monthchoosen.current(0) 
#monthchoosen.bind("<<ComboboxSelected>>", selected)
#selection = monthchoosen.get()

#combobox2
m = tk.StringVar() 
monthchoosen1 = ttk.Combobox(window, width = 27, textvariable = m) 
  
monthchoosen1['values'] = ('earnings',  
                          'product', 
                          'store', 
                          'seller',
                          'provider'
                          ) 
monthchoosen1.place(x=10, y=120 )

monthchoosen1.current(0) 

#окно ввода delete
entry1 = ttk.Entry()
entry1.place(x=210, y=200)
#кнопка для  удаления в таблицу
btn2 = Button(window, text="Delete", command=clickdelete)  
btn2.place(x=350, y=200)
#combobox2
p = tk.StringVar() 
monthchoosen2 = ttk.Combobox(window, width = 27, textvariable = p) 
  
monthchoosen2['values'] = ('earnings',  
                          'product', 
                          'store', 
                          'seller',
                          'provider'
                          ) 
monthchoosen2.place(x=10, y=200)

monthchoosen2.current(0) 

#кнопка для показа продавцов в таблицу
btn3 = Button(window, text="show sellers", command=clickf)  
btn3.place(x=200, y=280)

#окно ввода
entry2 = ttk.Entry()
entry2.place(x=50, y=280)

#кнопка для показа магазинов в таблицу
btn4 = Button(window, text="show shop", command=clickf2)  
btn4.place(x=200, y=360)

#окно ввода
entry3 = ttk.Entry()
entry3.place(x=50, y=360)

label1 = ttk.Label(text="Welcome", font=("Arial", 13))
label1.place(x=150, y=5)

label2 = ttk.Label(text="Here you can see the tables", font=("Arial", 10))
label2.place(x=10, y=30)

label3 = ttk.Label(text="Enter the data separated by a space to add it to the table", font=("Arial", 9))
label3.place(x=10, y=90)

label4 = ttk.Label(text="Enter the ID of the desired item to delete or the date in the table earnings", font=("Arial", 9))
label4.place(x=10, y=170)

label5 = ttk.Label(text="Enter the name of the store to find out the number of employees", font=("Arial", 9))
label5.place(x=10, y=250)
label6 = ttk.Label(text="Enter the employee's name and number to find out where he works", font=("Arial", 9))
label6.place(x=10, y=325)

window.mainloop()

conn.close()
