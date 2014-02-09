
class imsi_mon_start(object):

    
    def __init__(self, tmp_imsi_list):
        self.imsi_mon_start_str = ''
        self.imsi_list = tmp_imsi_list
    
    
    def get_imsi_mon_start_str(self):
        self.imsi_mon_start_str = 'xb1,' + self.imsi_list.get_imsi_list_str()
        return self.imsi_mon_start_str