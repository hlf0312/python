class imsi_list(object):

    
    def __init__(self):
        self.imsi_list = []
        self.imsi_list_str = ''
        self.imsi_list_max_len = 16
   
    
    def add_imsi(self, imsi):
        if(imsi.get_imsi_length() != '0'):
            self.imsi_list.append(imsi)
 
    
    def get_imsi_list_length(self):
        return len(self.imsi_list)
   
    
    def get_imsi_list_str(self):
        self.imsi_list_str = hex(self.get_imsi_list_length())[2:].upper()
        for i in self.imsi_list:
            self.imsi_list_str += ',' + i.get_imsi_str()
        self.imsi_list_str += ',00'*10*(self.imsi_list_max_len - self.get_imsi_list_length())
                
        return self.imsi_list_str
    
