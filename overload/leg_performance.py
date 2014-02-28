import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

a = fig.add_subplot(221)
y_cfcp_leg_performance = np.loadtxt('ran3000/CFCP_leg_performance')
#x_cfcp_performance = [i for i in range(len(y_cfcp_leg_performance))]
#cfcp_leg_performance, = a.plot(x_cfcp_performance, y_cfcp_leg_performance, label='cfcp')
cfcp_leg_performance, = a.plot(y_cfcp_leg_performance, label='cfcp')
handles, labels = a.get_legend_handles_labels()
a.set_xlabel('time')
a.set_ylabel('leg/s')
a.set_title('cfcp_leg_performance')
a.legend(handles[::-1], labels[::-1], loc=5)
#plt.grid()
#You can press g to show grid

a = fig.add_subplot(222)
y_uscp_1_leg_performance = np.loadtxt('ran3000/USCP-1_leg_performance')
x_uscp_1_leg_performance = [i for i in range(len(y_uscp_1_leg_performance))]
y_uscp_4_leg_performance = np.loadtxt('ran3000/USCP-4_leg_performance')
x_uscp_4_leg_performance = [i for i in range(len(y_uscp_4_leg_performance))]
uscp_1_leg_performance, = a.plot(x_uscp_1_leg_performance, y_uscp_1_leg_performance, label='uscp_1')
uscp_4_leg_performance, = a.plot(x_uscp_4_leg_performance, y_uscp_4_leg_performance, label='uscp_4')
handles, labels = a.get_legend_handles_labels()
a.set_xlabel('time')
a.set_ylabel('leg/s')
a.set_title('uscp_leg_performance')
a.legend(handles[::-1], labels[::-1], loc=5)
plt.grid()

a = fig.add_subplot(223)
y_wo_cpu_load = np.loadtxt('ran3000/CFPU-0_cpu_load_cacprb')
x_wo_cpu_load = [i for i in range(len(y_wo_cpu_load))]
y_sp_cpu_load = np.loadtxt('ran3000/CFPU-1_cpu_load_cacprb')
x_sp_cpu_load = [i for i in range(len(y_sp_cpu_load))]
wo_cac, = a.plot(x_wo_cpu_load, y_wo_cpu_load, label='wo_cac')
sp_cac, = a.plot(x_sp_cpu_load, y_sp_cpu_load, label='sp_cac')
handles, labels = a.get_legend_handles_labels()
a.legend(handles[::-1], labels[::-1], loc=5)
a.set_xlabel('time')
a.set_ylabel('%')
a.set_title('cfpu_cpu_load_cacprb')
plt.grid()

a = fig.add_subplot(224)
y_wo_cac_load = np.loadtxt('ran3000/CFPU-0_message_queue_cacprb')
x_wo_cac_load = [i for i in range(len(y_wo_cac_load))]
y_sp_cac_load = np.loadtxt('ran3000/CFPU-1_message_queue_cacprb')
x_sp_cac_load = [i for i in range(len(y_sp_cac_load))]
a.plot(x_wo_cac_load, y_wo_cac_load, label='wo_cac')
a.plot(x_sp_cac_load, y_sp_cac_load, label='sp_cac')
handles, labels = a.get_legend_handles_labels()
a.legend(handles[::-1], labels[::-1], loc=2)
a.set_xlabel('time')
a.set_ylabel('blk')
a.set_title('message_queue_cacprb')
plt.grid()

plt.show()