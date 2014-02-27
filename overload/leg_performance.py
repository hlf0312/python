import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

ax_cfcp_leg_performance = fig.add_subplot(221)
y_cfcp_leg_performance = np.loadtxt('ran3000/CFCP_leg_performance')
x_cfcp_performance = [i for i in range(len(y_cfcp_leg_performance))]
cfcp_leg_performance, = ax_cfcp_leg_performance.plot(x_cfcp_performance, y_cfcp_leg_performance, label='cfcp')
handles, labels = ax_cfcp_leg_performance.get_legend_handles_labels()
ax_cfcp_leg_performance.set_xlabel('time')
ax_cfcp_leg_performance.set_ylabel('leg/s')
ax_cfcp_leg_performance.set_title('cfcp_leg_performance')
ax_cfcp_leg_performance.legend(handles[::-1], labels[::-1], loc=5)
#plt.grid()

ax_uscp_leg_performance = fig.add_subplot(222)
y_uscp_1_leg_performance = np.loadtxt('ran3000/USCP-1_leg_performance')
x_uscp_1_leg_performance = [i for i in range(len(y_uscp_1_leg_performance))]
y_uscp_4_leg_performance = np.loadtxt('ran3000/USCP-4_leg_performance')
x_uscp_4_leg_performance = [i for i in range(len(y_uscp_4_leg_performance))]
uscp_1_leg_performance, = ax_uscp_leg_performance.plot(x_uscp_1_leg_performance, y_uscp_1_leg_performance, label='uscp_1')
uscp_4_leg_performance, = ax_uscp_leg_performance.plot(x_uscp_4_leg_performance, y_uscp_4_leg_performance, label='uscp_4')
handles, labels = ax_uscp_leg_performance.get_legend_handles_labels()
ax_uscp_leg_performance.set_xlabel('time')
ax_uscp_leg_performance.set_ylabel('leg/s')
ax_uscp_leg_performance.set_title('uscp_leg_performance')
ax_uscp_leg_performance.legend(handles[::-1], labels[::-1], loc=5)
plt.grid()

ax_cfpu_cpu_load_cacprb = fig.add_subplot(223)
y_wo_cpu_load = np.loadtxt('ran3000/CFPU-0_cpu_load_cacprb')
x_wo_cpu_load = [i for i in range(len(y_wo_cpu_load))]
y_sp_cpu_load = np.loadtxt('ran3000/CFPU-1_cpu_load_cacprb')
x_sp_cpu_load = [i for i in range(len(y_sp_cpu_load))]
wo_cac, = ax_cfpu_cpu_load_cacprb.plot(x_wo_cpu_load, y_wo_cpu_load, label='wo_cac')
sp_cac, = ax_cfpu_cpu_load_cacprb.plot(x_sp_cpu_load, y_sp_cpu_load, label='sp_cac')
handles, labels = ax_cfpu_cpu_load_cacprb.get_legend_handles_labels()
ax_cfpu_cpu_load_cacprb.legend(handles[::-1], labels[::-1], loc=5)
ax_cfpu_cpu_load_cacprb.set_xlabel('time')
ax_cfpu_cpu_load_cacprb.set_ylabel('%')
ax_cfpu_cpu_load_cacprb.set_title('cfpu_cpu_load_cacprb')
plt.grid()

ax_cfpu_0_message_queue_cacprb = fig.add_subplot(224)
y_wo_cac_load = np.loadtxt('ran3000/CFPU-0_message_queue_cacprb')
x_wo_cac_load = [i for i in range(len(y_wo_cac_load))]
y_sp_cac_load = np.loadtxt('ran3000/CFPU-1_message_queue_cacprb')
x_sp_cac_load = [i for i in range(len(y_sp_cac_load))]
ax_cfpu_0_message_queue_cacprb.plot(x_wo_cac_load, y_wo_cac_load, label='wo_cac')
ax_cfpu_0_message_queue_cacprb.plot(x_sp_cac_load, y_sp_cac_load, label='sp_cac')
handles, labels = ax_cfpu_0_message_queue_cacprb.get_legend_handles_labels()
ax_cfpu_0_message_queue_cacprb.legend(handles[::-1], labels[::-1], loc=2)
ax_cfpu_0_message_queue_cacprb.set_xlabel('time')
ax_cfpu_0_message_queue_cacprb.set_ylabel('blk')
ax_cfpu_0_message_queue_cacprb.set_title('message_queue_cacprb')
plt.grid()

plt.show()