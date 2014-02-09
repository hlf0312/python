
class imsi(object):
    
    def __init__(self, imsi, mon_dir):
        self.imsi = imsi
        self.imsi_table = ''
        self.mon_dir = mon_dir
        self.imsi_length = str(len(self.imsi))
        self.imsi_max_length = 16

    
    def get_imsi_table_str(self):
        if len(self.imsi)%2 == 0:
            for i in range(len(self.imsi)):
                if i%2 == 0:
                    if (i+2<len(self.imsi)):
                        self.imsi_table += self.imsi[i:i+2] + ','
                    else:
                        self.imsi_table += self.imsi[i:i+2]
            self.imsi_table += ',00'*((self.imsi_max_length-len(self.imsi))/2)
        else:
            for i in range(len(self.imsi)):
                if i%2 == 0 and (i+1<len(self.imsi)):
                    self.imsi_table += self.imsi[i:i+2] + ','
            self.imsi_table += self.imsi[len(self.imsi) - 1] + '0' + ',00'*((self.imsi_max_length-len(self.imsi))/2)        
        return self.imsi_table

    
    def get_imsi_length(self):
        return self.imsi_length

    
    def get_imsi_mon_dir(self):
        return self.mon_dir

    
    def get_imsi_str(self):
        return hex(int(self.get_imsi_length()))[2:].upper() + ',' + self.get_imsi_table_str() + ',' + self.get_imsi_mon_dir()
    