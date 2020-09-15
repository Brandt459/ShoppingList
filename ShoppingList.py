import tkinter as tk

root = tk.Tk()
root.title('Shopping List')
items = []


# Functions
def add_item():
    if item.get() == '':
        return
    if item.get() in items:
        return
    items.append(item.get())
    items_list.insert('end', item.get())


def delete_item():
    items.remove(items_list.get('anchor'))
    items_list.delete('anchor')


def clear():
    items.clear()
    items_list.delete(0, 'end')


tk.Label(root, text='Item').grid(row=0)

# Add Item Button
item = tk.Entry(root)
item.grid(row=0, column=1)
tk.Button(root, text='Add Item', command=add_item,
          width=10).grid(row=0, column=2)

# Items list
items_list = tk.Listbox(root)
items_list.grid(row=1, rowspan=2, column=1)

# Show items on GUI
for i in items:
    items_list.insert('end', i)

# Add buttons
tk.Button(root, text='Delete Item', command=delete_item,
          width=10, height=4).grid(row=1, column=2)
tk.Button(root, text='Clear', command=clear,
          width=10, height=4).grid(row=2, column=2)
tk.Button(root, text='Quit', command=root.quit, width=10, height=2).grid(
    row=3, column=2, sticky=tk.W)

root.mainloop()
