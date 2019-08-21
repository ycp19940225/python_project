#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk

# 第1步，实例化object，建立窗口window
windows = tk.Tk()

# 第2步，给窗口的可视化起名字
windows.title('测试窗口')

# 第3步，设定窗口的大小(长 * 宽)
windows.geometry('500x400')

# 第4步，在图形界面上设定标签
var = tk.StringVar()
label = tk.Label(windows, textvariable=var, bg='green', font=('Arial', 12), width=30, height=2)

label.pack()

def hit_me():
    varGet = lb.get(lb.curselection())
    var.set(varGet)

b = tk.Button(windows, text = 'hi' , font=('Arial', 12), width=10, height=1, command= hit_me)
b.pack()


var2 = tk.StringVar()
var2.set((1, 2, 3, 4))

# 创建listBox

lb = tk.Listbox(windows,listvariable=var2)

list_items = ['2222', 'cafaf', 'afa']

for item in list_items:
    lb.insert('end', item)

lb.insert(1, 'first')

lb.pack()

windows.mainloop()

