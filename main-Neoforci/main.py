# -*- coding : utf-8 -*-

# main.py

#========================================#

#import

import os;
import glob;
import threading;
import subprocess;
from scan_jar import scan_jar_file;
from print_log import w_log;

w_log("main_log", "INFO", "main.py启动 √ ");

w_log("main_log", "INFO", "导入完成 √ ");

#========================================#

run_path = os.getcwd();
jar_files = glob.glob("*.jar");

w_log("main_log", "INFO", "run_path，jar_files 初始化完成 √ ");

#========================================#

#code

def main():
    w_log("main_log", "INFO", "main.py 的 main 函数启动 √ ");

    w_log("main_log", "INFO", "启动扫描线程 √ ");

    monitor = threading.Thread(target=scan_jar_file);
    monitor.start();
    monitor.join();

    w_log("main_log", "INFO", "扫描完成 √ ");

    w_log("main_log", "INFO", "拉起main.java √ ");

    subprocess.run(["java", "main", "mod_data.json"], cwd=run_path);

    w_log("main_log", "INFO", "拉起完成 √ ");
    

#========================================#

if __name__ == "__main__":
    main();
