from mon_imsi_demo.imsi_list import imsi_list
from mon_imsi_demo.imsi import imsi
from mon_imsi_demo.imsi_mon_start import imsi_mon_start
from Tkinter import Tk, Text, Entry, StringVar, Label, Button


class imsi_mon_demo(object):

    
    def __init__(self):
        self.imsi_mon_str = 'dmxsendcli -h *,100,54F,0,0,4,0,C2E9,'
        self.imsi_list = imsi_list()
        self.imsi_mon_start = imsi_mon_start(self.imsi_list)
        
        self.imsi_val_1_row = 0
        self.imsi_val_2_row = self.imsi_val_1_row + 1
        self.imsi_val_3_row = self.imsi_val_2_row + 1
        self.imsi_val_4_row = self.imsi_val_3_row + 1
        self.imsi_val_5_row = self.imsi_val_4_row + 1
        self.imsi_val_6_row = self.imsi_val_5_row + 1
        self.imsi_val_7_row = self.imsi_val_6_row + 1
        self.imsi_val_8_row = self.imsi_val_7_row + 1
        self.dmx_output_row = self.imsi_val_8_row + 2
        
        self.root = Tk()
        self.root.wm_title("IMSI List notify")
        
        # valid percent substitutions (from the Tk entry man page)
        # %d = Type of action (1=insert, 0=delete, -1 for others)
        # %i = index of char string to be inserted/deleted, or -1
        # %P = value of the entry if the edit is allowed
        # %s = value of entry prior to editing
        # %S = the text string being inserted or deleted, if any
        # %v = the type of validation that is currently set
        # %V = the type of validation that triggered the callback
        #      (key, focusin, focusout, forced)
        # %W = the tk name of the widget
        vcmd = (self.root.register(self.OnValidate), 
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.label_imsi_val_1 = Label (self.root, text= "imsi_val[0]")
        self.label_imsi_val_1.grid(row=self.imsi_val_1_row)
        self.imsi_val_1_text = StringVar()
#         self.imsi_val_1_text.set('ffff')
        Entry(self.root, textvariable=self.imsi_val_1_text, validate="key", validatecommand=vcmd).grid(row=0, column=1)

        self.label_imsi_val_2 = Label (self.root, text= "imsi_val[1]")
        self.label_imsi_val_2.grid(row=self.imsi_val_2_row)
        self.imsi_val_2_text = StringVar()
        Entry(self.root, textvariable=self.imsi_val_2_text, validate="key", validatecommand=vcmd).grid(row=1, column=1)
        
        self.label_imsi_val_3 = Label (self.root, text= "imsi_val[2]")
        self.label_imsi_val_3.grid(row=self.imsi_val_3_row)
        self.imsi_val_3_text = StringVar()
        Entry(self.root, textvariable=self.imsi_val_3_text, validate="key", validatecommand=vcmd).grid(row=2, column=1)

        self.label_imsi_val_4 = Label (self.root, text= "imsi_val[3]")
        self.label_imsi_val_4.grid(row=self.imsi_val_4_row)
        self.imsi_val_4_text = StringVar()
        Entry(self.root, textvariable=self.imsi_val_4_text, validate="key", validatecommand=vcmd).grid(row=3, column=1)

        self.label_imsi_val_5 = Label (self.root, text= "imsi_val[4]")
        self.label_imsi_val_5.grid(row=self.imsi_val_5_row)
        self.imsi_val_5_text = StringVar()
        Entry(self.root, textvariable=self.imsi_val_5_text, validate="key", validatecommand=vcmd).grid(row=4, column=1)

        self.label_imsi_val_6 = Label (self.root, text= "imsi_val[5]")
        self.label_imsi_val_6.grid(row=self.imsi_val_6_row)
        self.imsi_val_6_text = StringVar()
        Entry(self.root, textvariable=self.imsi_val_6_text, validate="key", validatecommand=vcmd).grid(row=5, column=1)

        self.label_imsi_val_7 = Label (self.root, text= "imsi_val[6]")
        self.label_imsi_val_7.grid(row=self.imsi_val_7_row)
        self.imsi_val_7_text = StringVar()
        Entry(self.root, textvariable=self.imsi_val_7_text, validate="key", validatecommand=vcmd).grid(row=6, column=1)

        self.label_imsi_val_8 = Label (self.root, text= "imsi_val[7]")
        self.label_imsi_val_8.grid(row=self.imsi_val_8_row)
        self.imsi_val_8_text = StringVar()
        Entry(self.root, textvariable=self.imsi_val_8_text, validate="key", validatecommand=vcmd).grid(row=7, column=1)

        self.buttontext = StringVar()
        self.buttontext.set("Send")
        Button(self.root, textvariable=self.buttontext, command=self.send_handler).grid(row=8)
    
        self.root.mainloop()
    
    
    def get_imsi_mon_str(self):
        self.imsi_mon_str += self.imsi_mon_start.get_imsi_mon_start_str()
        return self.imsi_mon_str

    def reset_all_internal_str(self):
        self.imsi_mon_str = 'dmxsendcli -h *,100,54F,0,0,4,0,C2E9,'
        self.imsi_list = imsi_list()
        self.imsi_mon_start = imsi_mon_start(self.imsi_list)

    def gen_imsi_list(self):
        in_imsi_0 = self.imsi_val_1_text.get()
        in_imsi_1 = self.imsi_val_2_text.get()
        in_imsi_2 = self.imsi_val_3_text.get()
        in_imsi_3 = self.imsi_val_4_text.get()
        in_imsi_4 = self.imsi_val_5_text.get()
        in_imsi_5 = self.imsi_val_6_text.get()
        in_imsi_6 = self.imsi_val_7_text.get()
        in_imsi_7 = self.imsi_val_8_text.get()
        imsi_mon_dir_0 = '3'
        imsi_mon_dir_1 = '00'
        imsi_mon_dir_2 = '00'
        imsi_mon_dir_3 = '00'
        imsi_mon_dir_4 = '00'
        imsi_mon_dir_5 = '00'
        imsi_mon_dir_6 = '00'
        imsi_mon_dir_7 = '00'
        imsi_0 = imsi(in_imsi_0, imsi_mon_dir_0)
        imsi_1 = imsi(in_imsi_1, imsi_mon_dir_1)
        imsi_2 = imsi(in_imsi_2, imsi_mon_dir_2)
        imsi_3 = imsi(in_imsi_3, imsi_mon_dir_3)
        imsi_4 = imsi(in_imsi_4, imsi_mon_dir_4)
        imsi_5 = imsi(in_imsi_5, imsi_mon_dir_5)
        imsi_6 = imsi(in_imsi_6, imsi_mon_dir_6)
        imsi_7 = imsi(in_imsi_7, imsi_mon_dir_7)
        self.imsi_list.add_imsi(imsi_0)
        self.imsi_list.add_imsi(imsi_1)
        self.imsi_list.add_imsi(imsi_2)
        self.imsi_list.add_imsi(imsi_3)
        self.imsi_list.add_imsi(imsi_4)
        self.imsi_list.add_imsi(imsi_5)
        self.imsi_list.add_imsi(imsi_6)
        self.imsi_list.add_imsi(imsi_7)

    def send_handler(self):
        self.reset_all_internal_str()
        self.gen_imsi_list()
        text_height = 5
        text = Text(self.root, height=text_height)
        text.insert(1.0, self.get_imsi_mon_str())
        text.grid(row=self.dmx_output_row)
        
#         bcn_501_ip = '10.56.116.8'
#     #         ssh_ip = '10.68.156.43' 
#         client = paramiko.SSHClient() 
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
#         client.connect(bcn_501_ip, 22, username='root', password='root', timeout=4) 
#         stdin, stdout, stderr = client.exec_command(dmxsendcli) 
#         for std in stdout.readlines(): 
#             print std,
#         client.close() 
#         self.label.configure(text=result)
    
    def OnValidate(self, d, i, P, s, S, v, V, W):
        print "OnValidate:"
        print "d='%s'" % d
        print "i='%s'" % i
        print "P='%s'" % P
        print "s='%s'" % s
        print "S='%s'" % S
        print "v='%s'" % v
        print "V='%s'" % V
        print "W='%s'" % W
        return ((len(s)<=14) & (S>='0') & (S <= '9'))
    
if __name__ == '__main__':
    imsi_mon_demo()