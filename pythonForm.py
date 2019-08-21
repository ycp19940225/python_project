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

on_hit = False

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('1111')
    else:
        on_hit = True
        var.set('')

b = tk.Button(windows, text = 'hi' , font=('Arial', 12), width=10, height=1, command= hit_me)
b.pack()


e1 = tk.Entry(windows, show="", font=('Arial', 12))
e2 = tk.Entry(windows, show="", font=('Arial', 12))
e1.pack()
# e2.pack()

def insert_point():
    var1 = e1.get()
    t.insert('insert', var1)

def insert_end():
    var2 = e1.get()
    t.insert('end', var2)


b1 = tk.Button(windows, text='insert_point', font=('Arial', 12), width=10, height=1, command=insert_point)
b2 = tk.Button(windows, text='insert_end', font=('Arial', 12), width=10, height=1, command=insert_end)
b1.pack()
b2.pack()


t = tk.Text(windows, height=3)
t.pack()


windows.mainloop()

