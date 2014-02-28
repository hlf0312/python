#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import Tkinter as Tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

matplotlib.use('TkAgg')
root = Tk.Tk()
root.wm_title("Embedding in TK")

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
    y_cfcp_leg_performance = np.loadtxt('ran3000/CFCP_leg_performance')
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

button = Tk.Button(master=root, text='CFCP', command=show_cfcp_leg_performance)
button.pack(side=Tk.BOTTOM)


def draw_uscp_axis():
    y_uscp_1_leg_performance = np.loadtxt('ran3000/USCP-1_leg_performance') #    x_uscp_1_leg_performance = [i for i in range(len(y_uscp_1_leg_performance))]
    y_uscp_4_leg_performance = np.loadtxt('ran3000/USCP-4_leg_performance') #    x_uscp_4_leg_performance = [i for i in range(len(y_uscp_4_leg_performance))]
    a.plot(y_uscp_1_leg_performance, label='uscp_1')
    a.plot(y_uscp_4_leg_performance, label='uscp_4')
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

button = Tk.Button(master=root, text='USCP', command=show_uscp_leg_performance)
button.pack(side=Tk.BOTTOM)

def draw_cac_msg_queue_axis():
    y_wo_cac_load = np.loadtxt('ran3000/CFPU-0_message_queue_cacprb')
    y_sp_cac_load = np.loadtxt('ran3000/CFPU-1_message_queue_cacprb')
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

button = Tk.Button(master=root, text='CAC Queue', command=show_cac_queue_performance)
button.pack(side=Tk.BOTTOM)

def draw_cac_cpu_load_axis():
    y_wo_cpu_load = np.loadtxt('ran3000/CFPU-0_cpu_load_cacprb')
    y_sp_cpu_load = np.loadtxt('ran3000/CFPU-1_cpu_load_cacprb')
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

button = Tk.Button(master=root, text='CAC Load', command=show_cac_cpu_load)
button.pack(side=Tk.BOTTOM)

Tk.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.

