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

l = tk.Label(windows, text='      ', bg='green')
l.pack()

counter = 0
def do_job():
    pass

menuBar = tk.Menu(windows)

fileMenu = tk.Menu(menuBar, tearoff=0)

menuBar.add_cascade(label='文件', menu=fileMenu)

# 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
fileMenu.add_command(label='New', command=do_job)
fileMenu.add_command(label='Open', command=do_job)
fileMenu.add_command(label='Save', command=do_job)
fileMenu.add_separator()    # 添加一条分隔线
fileMenu.add_command(label='Exit', command=windows.quit)  # 用tkinter里面自带的quit()函数


# 编辑下拉

editMenu = tk.Menu(windows, tearoff=0)

menuBar.add_cascade(label='edit', menu=editMenu)

# 同样的在 Edit 中加入Cut、Copy、Paste等小命令功能单元，如果点击这些单元, 就会触发do_job的功能
editMenu.add_command(label='Cut', command=do_job)
editMenu.add_command(label='Copy', command=do_job)
editMenu.add_command(label='Paste', command=do_job)


# 第8步，创建第二级菜单，即菜单项里面的菜单
submenu = tk.Menu(fileMenu)  # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
fileMenu.add_cascade(label='Import', menu=submenu, underline=0)  # 给放入的菜单submenu命名为Import

# 第9步，创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）
submenu.add_command(label='Submenu_1', command=do_job)  # 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1

# 第11步，创建菜单栏完成后，配置让菜单栏menubar显示出来
windows.config(menu=menuBar)



windows.mainloop()

