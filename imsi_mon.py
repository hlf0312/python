
import paramiko
from Tkinter import *

class imsi_record(object):
    def __init__(self, imsi_value):
        self.record_imsi = [0,0,0,0,0,0,0,0]
        self.record_len = 0
        
        for i in range(8):
            self.record_imsi[i] = '0'
        
        for i in range(len(imsi_value)):
            self.record_imsi[i] = imsi_value[i]
        
        self.record_str = str(len(imsi_value))
        
        for i in range(8):
            self.record_str += ',' + self.record_imsi[i]
            
    def get_record(self):
        return self.record_str
    
    def get_record_len(self):
        for i in self.record_imsi:
            if i != '0':
                self.record_len += 1
        return self.record_len

class App(object):
    def __init__(self):
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
        self.label_imsi_val_1.grid(row=0)
        self.imsi_val_1_text = StringVar()
#         self.imsi_val_1_text.set('ffff')
        Entry(self.root, textvariable=self.imsi_val_1_text, validate="key", validatecommand=vcmd).grid(row=0, column=1)

        self.label_imsi_val_2 = Label (self.root, text= "imsi_val[1]")
        self.label_imsi_val_2.grid(row=1)
        self.imsi_val_2_text = StringVar()
        Entry(self.root, textvariable=self.imsi_val_2_text, validate="key", validatecommand=vcmd).grid(row=1, column=1)
        
        self.label_imsi_val_3 = Label (self.root, text= "imsi_val[2]")
        self.label_imsi_val_3.grid(row=2)
        self.imsi_val_3_text = StringVar()
        Entry(self.root, textvariable=self.imsi_val_3_text, validate="key", validatecommand=vcmd).grid(row=2, column=1)

        self.label_imsi_val_4 = Label (self.root, text= "imsi_val[3]")
        self.label_imsi_val_4.grid(row=3)
        self.imsi_val_4_text = StringVar()
        Entry(self.root, textvariable=self.imsi_val_4_text, validate="key", validatecommand=vcmd).grid(row=3, column=1)

        self.label_imsi_val_5 = Label (self.root, text= "imsi_val[4]")
        self.label_imsi_val_5.grid(row=4)
        self.imsi_val_5_text = StringVar()
        Entry(self.root, textvariable=self.imsi_val_5_text, validate="key", validatecommand=vcmd).grid(row=4, column=1)

        self.label_imsi_val_6 = Label (self.root, text= "imsi_val[5]")
        self.label_imsi_val_6.grid(row=5)
        self.imsi_val_6_text = StringVar()
        Entry(self.root, textvariable=self.imsi_val_6_text, validate="key", validatecommand=vcmd).grid(row=5, column=1)

        self.label_imsi_val_7 = Label (self.root, text= "imsi_val[6]")
        self.label_imsi_val_7.grid(row=6)
        self.imsi_val_7_text = StringVar()
        Entry(self.root, textvariable=self.imsi_val_7_text, validate="key", validatecommand=vcmd).grid(row=6, column=1)

        self.label_imsi_val_8 = Label (self.root, text= "imsi_val[7]")
        self.label_imsi_val_8.grid(row=7)
        self.imsi_val_8_text = StringVar()
        Entry(self.root, textvariable=self.imsi_val_8_text, validate="key", validatecommand=vcmd).grid(row=7, column=1)

        self.buttontext = StringVar()
        self.buttontext.set("Send")
        Button(self.root, textvariable=self.buttontext, command=self.clicked1).grid(row=8)

#         self.label = Label (self.root, text="")
#         self.label.grid(row=5)

        self.root.mainloop()

    def clicked1(self):
        imsi_record_list = []
        imsi_record_num = 0
        imsi_field_0 = self.imsi_val_1_text.get()
        imsi_field_1 = self.imsi_val_2_text.get()
        imsi_field_2 = self.imsi_val_3_text.get()
        imsi_field_3 = self.imsi_val_4_text.get()
        imsi_field_4 = self.imsi_val_5_text.get()
        imsi_field_5 = self.imsi_val_6_text.get()
        imsi_field_6 = self.imsi_val_7_text.get()
        imsi_field_7 = self.imsi_val_8_text.get()
        imsi_record_0 = imsi_record(imsi_field_0)
        imsi_record_1 = imsi_record(imsi_field_1)
        imsi_record_2 = imsi_record(imsi_field_2)
        imsi_record_3 = imsi_record(imsi_field_3)
        imsi_record_4 = imsi_record(imsi_field_4)
        imsi_record_5 = imsi_record(imsi_field_5)
        imsi_record_6 = imsi_record(imsi_field_6)
        imsi_record_7 = imsi_record(imsi_field_7)
        imsi_record_list.append(imsi_record_0)
        imsi_record_list.append(imsi_record_1)
        imsi_record_list.append(imsi_record_2)
        imsi_record_list.append(imsi_record_3)
        imsi_record_list.append(imsi_record_4)
        imsi_record_list.append(imsi_record_5)
        imsi_record_list.append(imsi_record_6)
        imsi_record_list.append(imsi_record_7)
        
        for i in imsi_record_list:
            if i.get_record_len() != 0:
                imsi_record_num += 1
                    
        dmxsendcli = 'dmxsendcli -h *,100,54F,0,0,4,0,C2E9'
        imsi_start_s = 'xb' + str(imsi_record_num)       + \
                        ',' + imsi_record_0.get_record() + \
                        ',' + imsi_record_1.get_record() + \
                        ',' + imsi_record_2.get_record() + \
                        ',' + imsi_record_3.get_record() + \
                        ',' + imsi_record_4.get_record() + \
                        ',' + imsi_record_5.get_record() + \
                        ',' + imsi_record_6.get_record() + \
                        ',' + imsi_record_7.get_record()
                         
        result = dmxsendcli + ',' + imsi_start_s
        text = Text(self.root, height=5)
        text.insert(1.0, result)
        text.grid(row=9)
        
        bcn_501_ip = '10.56.116.8'
#         ssh_ip = '10.68.156.43' 
        client = paramiko.SSHClient() 
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        client.connect(bcn_501_ip, 22, username='root', password='root', timeout=4) 
        stdin, stdout, stderr = client.exec_command(dmxsendcli) 
        for std in stdout.readlines(): 
            print std,
        client.close() 
#         self.label.configure(text=result)

    def button_click(self, e):
        pass
    
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
        return ((len(s)<=7) & (((S <= 'f') & (S >='a')) | ((S>='A') & (S <= 'F')) | ((S>='0') & (S <= '9'))))

App()    

# if __name__ == '__main__':
#     pass