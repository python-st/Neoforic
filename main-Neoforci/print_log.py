# -*- coding : utf-8 -*-

# print_log.py

#========================================#

#import

from datetime import datetime;

#========================================#

#code

def w_log(file_name, type, event):
    with open(file_name+".log", "a+") as log_file :
        now_time = datetime.now().strftime("%Y-%m-%d H: %H-%M-%S.%f")[:-3];
        log_s = "[" + now_time + "] " + " [" +type + "] " + event;
        log_file.write(f"{log_s} \n");

# DEBUG INFO WARN ERROR FATAL

#========================================#

if __name__ == "__main__":
    print("怎么可能");