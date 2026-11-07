# -*- coding : utf-8 -*-

#========================================#

#import

import os;
import glob;
import json;
import threading;
import zipfile;
import re;

#========================================#

run_path = os.getcwd();
jar_files = glob.glob("*.jar")

#========================================#

def scan_jar_file():
    
    for jar_path in jar_files:
        
        try:
            with zipfile.ZipFile(jar_path, 'r') as jar:
                file_list = jar.namelist();
                
                # 1.Fabric
                if "fabric.mod.json" in file_list:
                    content = jar.read("fabric.mod.json").decode('utf-8', errors='ignore');
                    # 提取 fabric 的 id
                    id_match = re.search(r'"id"\s*:\s*"([^"]+)"', content);
                    mod_id = id_match.group(1) if id_match else "Unknown";
                    print(f"[Fabric] 文件: {jar_path} | ID: {mod_id}");
                    continue;
                
                # 2.NeoForge
                if "META-INF/neoforge.mods.toml" in file_list:
                    content = jar.read("META-INF/neoforge.mods.toml").decode('utf-8', errors='ignore');
                    id_match = re.search(r'modId\s*=\s*"([^"]+)"', content);
                    mod_id = id_match.group(1) if id_match else "Unknown";
                    print(f"[NeoForge] 文件: {jar_path} | ID: {mod_id}");
                    continue;
                
                if "META-INF/mods.toml" in file_list:
                    toml_content = jar.read("META-INF/mods.toml").decode('utf-8', errors='ignore');
                    
                    # mods.toml - id
                    id_match = re.search(r'modId\s*=\s*"([^"]+)"', toml_content);
                    mod_id = id_match.group(1) if id_match else "Unknown";

                    # 3a.neoforge
                    if re.search(r'modId\s*=\s*"neoforge"', toml_content) or "NeoForge" in toml_content:
                        print(f"[NeoForge] 文件: {jar_path} | ID: {mod_id}");
                        continue;
                    
                    # 3b.Forge
                    print(f"[Forge] 文件: {jar_path} | ID: {mod_id}");
                    continue;
                
                print(f"[Unknown] 文件: {jar_path}");

        except zipfile.BadZipFile:
            print(f"[Error] {jar_path} - 损坏的压缩包");
        except Exception as e:
            print(f"[Error] {jar_path} - {str(e)}");

#========================================#

def main():
    monitor = threading.Thread(target=scan_jar_file);
    monitor.start();
    monitor.join();

#========================================#

if __name__ == "__main__":
    main();