import tkinter as tk

root = tk.Tk()
root.title('Shopping List')
items = []


def addItem():
    if item.get() == '':
        return
    if item.get() in items:
        return
    items.append(item.get())
    items_list.insert('end', item.get())


def deleteItem():
    items_list.delete('anchor')


def clear():
    items_list.delete(0, 'end')


tk.Label(root, text='Item').grid(row=0)

# Add Item Button
item = tk.Entry(root)
item.grid(row=0, column=1)
tk.Button(root, text='Add Item', command=addItem).grid(row=0, column=2)

# Items list
items_list = tk.Listbox(root)
items_list.grid(row=1, rowspan=2, column=1)

# Show items on GUI
for i in items:
    items_list.insert('end', i)

tk.Button(root, text='Delete Item', command=deleteItem).grid(row=1, column=2)

tk.Button(root, text='Clear', command=clear).grid(row=2, column=2)

tk.Button(root, text='Quit', command=root.quit).grid(
    row=3, column=2, sticky=tk.W)

root.mainloop()
