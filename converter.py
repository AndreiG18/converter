import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

'''Take current rates from https://cursbnr.ro/
    
'''
r = requests.get('https://cursbnr.ro/')
soup = BeautifulSoup(r.content, 'lxml')
table = soup.find('table', {'id': 'table-currencies'}).tbody
currency = {}
for tr in table.find_all('tr'):
    td = tr.find_all('td')
    currency[td[0].text] = [float(td[2].text)]
currency["RON"] = [1]

'''List for dropbox'''
data = []
for i, item in enumerate(currency.keys()):
    data.append(item)

def convert():
    '''Convert a sum from selected input to selected output'''
    amount = int(text_1.get())
    value = mfrom.get()
    value2 = mto.get()
    if value != 'RON':
        amount = amount * currency[value][0]
    amount = round(amount / currency[value2][0], 2)
    total_1.config(text= amount)





root = tk.Tk()
root.title("CurrencyConvertor")
root.geometry('500x100')

'''Input sum widget'''
text_1 = tk.Entry(root)
text_1.grid_configure(column= 0, row= 1)

'''Selection widgets'''
mfrom = ttk.Combobox(root,values= data,)
mfrom.grid_configure(column= 1, row= 1)

mto = ttk.Combobox(root, values= data,)
mto.grid_configure(column= 5, row= 1)


'''Labels'''
label = tk.Label(root, text="Amount", font="Arial,16")
label.grid_configure(column= 0, row= 0)

label = tk.Label(root, text="From", font="Arial,16")
label.grid_configure(column= 1, row= 0)

label_1 = tk.Label(root, text= "Total" ,font= "Arial, 16")
label_1.grid_configure(column= 4, row= 0)

label_2 = tk.Label(root, text= "In" ,font= "Arial, 16")
label_2.grid_configure(column= 5, row= 0)

total_1 = tk.Label(root, text= "")
total_1.grid_configure(column= 4, row= 1)


'''Conversion button'''
button = tk.Button(root, text= "Convert", command= convert)
button.grid_configure(column= 1, row= 2)


root.grid()

root.mainloop()




