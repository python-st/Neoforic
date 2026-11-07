# -*- coding : utf-8 -*-

#========================================#

#import

import os;
import glob;
import json;
import threading;
from scan_jar import scan_jar_file;

#========================================#

run_path = os.getcwd();
jar_files = glob.glob("*.jar")

#========================================#

#code

def main():
    monitor = threading.Thread(target=scan_jar_file);
    monitor.start();
    monitor.join();

#========================================#

if __name__ == "__main__":
    main();
