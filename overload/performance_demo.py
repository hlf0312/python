#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import Tkinter as Tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import tkFileDialog as filedialog

matplotlib.use('TkAgg')
root = Tk.Tk()
root.wm_title("RAN3000")

frame_buttons=Tk.Frame(root)

f = plt.Figure(figsize=(5,4), dpi=100)
a = f.add_subplot(111)

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg( canvas, root )
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

axis_show_flag_dic={'uscp'       :  False,
                    'cfcp'       :  False,
                    'cac_queue'  :  False,
                    'cac_load'   :  False
                    }

def clear_axis(input_axis):
    a.cla()
    if input_axis == 'all':
        for i in axis_show_flag_dic.keys():
            axis_show_flag_dic[i] = False
    else:    
        axis_show_flag_dic[input_axis]=False

def get_axis_show_flag(input_axis):
    return axis_show_flag_dic[input_axis]

def set_axis_show_flag(input_axis):
    axis_show_flag_dic[input_axis]=True

def draw_cfcp_axis():
    y_cfcp_leg_performance = np.loadtxt(open_file_path_dic['cfcp'])
    a.plot(y_cfcp_leg_performance, label='cfcp')
    handles, labels = a.get_legend_handles_labels()
    a.set_xlabel('time')
    a.set_ylabel('leg/s')
    a.set_title('cfcp_leg_performance')
    a.legend(handles[::-1], labels[::-1], loc=5)

def show_cfcp_leg_performance():
    clear_axis('all')
    if get_axis_show_flag('cfcp'):
        clear_axis('cfcp')
    else:
        set_axis_show_flag('cfcp')
        draw_cfcp_axis()
    canvas.show()


def draw_uscp_axis():
    y_uscp_A_leg_performance = np.loadtxt(open_file_path_dic['uscp_A']) #    x_uscp_1_leg_performance = [i for i in range(len(y_uscp_A_leg_performance))]
    y_uscp_B_leg_performance = np.loadtxt(open_file_path_dic['uscp_B']) #    x_uscp_4_leg_performance = [i for i in range(len(y_uscp_B_leg_performance))]
    a.plot(y_uscp_A_leg_performance, label='uscp_A')
    a.plot(y_uscp_B_leg_performance, label='uscp_B')
    handles, labels = a.get_legend_handles_labels()
    a.set_xlabel('time')
    a.set_ylabel('leg/s')
    a.set_title('uscp_leg_performance')
    a.legend(handles[::-1], labels[::-1], loc=5)

def show_uscp_leg_performance():
    clear_axis('all')
    if get_axis_show_flag('uscp'):
        clear_axis('uscp')
    else:
        set_axis_show_flag('uscp')
        draw_uscp_axis()
    canvas.show()

def draw_cac_msg_queue_axis():
    y_wo_cac_load = np.loadtxt(open_file_path_dic['wo_cac_queue'])
    y_sp_cac_load = np.loadtxt(open_file_path_dic['sp_cac_queue'])
    a.plot(y_wo_cac_load, label='wo_cac')
    a.plot(y_sp_cac_load, label='sp_cac')
    handles, labels = a.get_legend_handles_labels()
    a.legend(handles[::-1], labels[::-1], loc=2)
    a.set_xlabel('time')
    a.set_ylabel('blk')
    a.set_title('message_queue_cacprb')

def show_cac_queue_performance():
    clear_axis('all')
    if get_axis_show_flag('cac_queue'):
        clear_axis('cac_queue')
    else:
        set_axis_show_flag('cac_queue')
        draw_cac_msg_queue_axis()
    canvas.show()

def draw_cac_cpu_load_axis():
    y_wo_cpu_load = np.loadtxt(open_file_path_dic['wo_cac_load'])
    y_sp_cpu_load = np.loadtxt(open_file_path_dic['sp_cac_load'])
    a.plot(y_wo_cpu_load, label='wo_cac')
    a.plot(y_sp_cpu_load, label='sp_cac')
    handles, labels = a.get_legend_handles_labels()
    a.legend(handles[::-1], labels[::-1], loc=5)
    a.set_xlabel('time')
    a.set_ylabel('%')
    a.set_title('cfpu_cpu_load_cacprb')

def show_cac_cpu_load():
    clear_axis('all')
    if get_axis_show_flag('cac_load'):
        clear_axis('cac_load')
    else:
        set_axis_show_flag('cac_load')
        draw_cac_cpu_load_axis()
    canvas.show()

cfcp_button = Tk.Button(frame_buttons, text='CFCP', command=show_cfcp_leg_performance)
cfcp_button.grid(row=1, column=1, ipadx=12)

uscp_button = Tk.Button(frame_buttons, text='USCP', command=show_uscp_leg_performance)
uscp_button.grid(row=1, column=2, ipadx=18)

cac_load_button = Tk.Button(frame_buttons, text='CAC Load', command=show_cac_cpu_load)
cac_load_button.grid(row=2, column=1)

cac_queue_button = Tk.Button(frame_buttons, text='CAC Queue', command=show_cac_queue_performance)
cac_queue_button.grid(row=2, column=2)

#Frame Button set location
frame_buttons.pack(side=Tk.BOTTOM)

frame_open_file=Tk.Frame(root)
frame_open_file.pack(side=Tk.LEFT)

cfcp_open_lable=Tk.Label(frame_open_file, text='CFCP')
cfcp_open_lable.grid(row=1, column=1)
cfcp_open_entry = Tk.Entry(frame_open_file, width=40)
cfcp_open_entry.grid(row=1, column=2)
cfcp_open_button = Tk.Button(frame_open_file,text="Open",command=lambda:open_file('cfcp'))
cfcp_open_button.grid(row=1, column=3)

uscp_A_open_lable=Tk.Label(frame_open_file, text='USCP_A')
uscp_A_open_lable.grid(row=1, column=4)
uscp_A_open_entry = Tk.Entry(frame_open_file, width=40)
uscp_A_open_entry.grid(row=1, column=5)
uscp_A_open_button = Tk.Button(frame_open_file,text="Open",command=lambda:open_file('uscp_A'))
uscp_A_open_button.grid(row=1, column=6)

uscp_B_open_lable=Tk.Label(frame_open_file, text='USCP_B')
uscp_B_open_lable.grid(row=2, column=1)
uscp_B_open_entry = Tk.Entry(frame_open_file, width=40)
uscp_B_open_entry.grid(row=2, column=2)
uscp_B_open_button = Tk.Button(frame_open_file,text="Open",command=lambda:open_file('uscp_B'))
uscp_B_open_button.grid(row=2, column=3)

wo_cac_queue_open_lable=Tk.Label(frame_open_file, text='WO CAC Queue')
wo_cac_queue_open_lable.grid(row=2, column=4)
wo_cac_queue_open_entry = Tk.Entry(frame_open_file, width=40)
wo_cac_queue_open_entry.grid(row=2, column=5)
wo_cac_queue_open_button = Tk.Button(frame_open_file,text="Open",command=lambda:open_file('wo_cac_queue'))
wo_cac_queue_open_button.grid(row=2, column=6)

sp_cac_queue_open_lable=Tk.Label(frame_open_file, text='SP CAC Queue')
sp_cac_queue_open_lable.grid(row=3, column=1)
sp_cac_queue_open_entry = Tk.Entry(frame_open_file, width=40)
sp_cac_queue_open_entry.grid(row=3, column=2)
sp_cac_queue_open_button = Tk.Button(frame_open_file,text="Open",command=lambda:open_file('sp_cac_queue'))
sp_cac_queue_open_button.grid(row=3, column=3)

wo_cac_load_open_lable=Tk.Label(frame_open_file, text='WO CAC Load')
wo_cac_load_open_lable.grid(row=3, column=4)
wo_cac_load_open_entry = Tk.Entry(frame_open_file, width=40)
wo_cac_load_open_entry.grid(row=3, column=5)
wo_cac_load_open_button = Tk.Button(frame_open_file,text="Open",command=lambda:open_file('wo_cac_load'))
wo_cac_load_open_button.grid(row=3, column=6)

sp_cac_load_open_lable=Tk.Label(frame_open_file, text='SP CAC Load')
sp_cac_load_open_lable.grid(row=4, column=1)
sp_cac_load_open_entry = Tk.Entry(frame_open_file, width=40)
sp_cac_load_open_entry.grid(row=4, column=2)
sp_cac_load_open_button = Tk.Button(frame_open_file,text="Open",command=lambda:open_file('sp_cac_load'))
sp_cac_load_open_button.grid(row=4, column=3)

def open_file(arg):
    open_entry_dic[arg].delete(0,Tk.END)
    open_file_path_dic[arg] = filedialog.askopenfilename() 
    if open_file_path_dic[arg]:
        open_entry_dic[arg].insert(0, open_file_path_dic[arg])

open_entry_dic = {'cfcp'        :   cfcp_open_entry,
                 'uscp_A'       :   uscp_A_open_entry,
                 'uscp_B'       :   uscp_B_open_entry,
                 'wo_cac_queue' :   wo_cac_queue_open_entry,
                 'sp_cac_queue' :   sp_cac_queue_open_entry,
                 'wo_cac_load'  :   wo_cac_load_open_entry,
                 'sp_cac_load'  :   sp_cac_load_open_entry
                 }

open_file_path_dic = {'cfcp'        :   'ran3000/CFCP_leg_performance',
                     'uscp_A'       :   'ran3000/USCP-1_leg_performance',
                     'uscp_B'       :   'ran3000/USCP-4_leg_performance',
                     'wo_cac_queue' :   'ran3000/CFPU-0_message_queue_cacprb',
                     'sp_cac_queue' :   'ran3000/CFPU-1_message_queue_cacprb',
                     'wo_cac_load'  :   'ran3000/CFPU-0_cpu_load_cacprb',
                     'sp_cac_load'  :   'ran3000/CFPU-1_cpu_load_cacprb'
                     }

Tk.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.

