#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import ImageTk

# 第1步，实例化object，建立窗口window
windows = tk.Tk()

# 第2步，给窗口的可视化起名字
windows.title('测试窗口')

# 第3步，设定窗口的大小(长 * 宽)
windows.geometry('500x400')

canvas = tk.Canvas(windows, bg='green', height=200, width=500)

# imageFile = tk.PhotoImage(file='test.jpg')
imageFile = ImageTk.PhotoImage(file='test.jpg')
image = canvas.create_image(250, 0, anchor='n', image=imageFile)

# 定义参数画出图形
# 定义多边形参数，然后在画布上画出指定图形
x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)                   # 画直线
oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')  # 画圆 用黄色填充
arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=180)      # 画扇形 从0度打开收到180度结束
rect = canvas.create_rectangle(330, 30, 330+20, 30+20)                  # 画矩形正方形
canvas.pack()

def move_img():
    canvas.move(oval, 2, 2)


tk.Button(windows, text='移动图像', command=move_img).pack()


windows.mainloop()

