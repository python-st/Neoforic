# -*- coding : utf-8 -*-

#========================================#

#import

import glob;
import zipfile;
import re;
import os;
from write_json import write_json_append;

#========================================#

jar_files = glob.glob("*.jar")

#========================================#

#code

def scan_jar_file():

    if os.path.exists("mod_data.json"):
        os.remove("mod_data.json");
   
    for jar_path in jar_files:
        
        try:
            with zipfile.ZipFile(jar_path, 'r') as jar:
                file_list = jar.namelist();
                
                # 1.Fabric
                if "fabric.mod.json" in file_list:
                    content = jar.read("fabric.mod.json").decode('utf-8', errors='ignore');
                    # fabric - id
                    id_match = re.search(r'"id"\s*:\s*"([^"]+)"', content);
                    mod_id = id_match.group(1) if id_match else "Unknown";
                    data_2 = {"type": "Fabric", "id": mod_id, "jar_path": jar_path};
                    write_json_append(data_2, "mod_data.json");
                    print(f"[Fabric] 文件: {jar_path} - ID: {mod_id}");
                    continue;
                
                # 2.NeoForge
                if "META-INF/neoforge.mods.toml" in file_list:
                    content = jar.read("META-INF/neoforge.mods.toml").decode('utf-8', errors='ignore');
                    id_match = re.search(r'modId\s*=\s*"([^"]+)"', content);
                    mod_id = id_match.group(1) if id_match else "Unknown";
                    data_2 = {"type": "NeoForge", "id": mod_id, "jar_path": jar_path};
                    write_json_append(data_2, "mod_data.json");
                    print(f"[NeoForge] 文件: {jar_path} - ID: {mod_id}");
                    continue;
                
                if "META-INF/mods.toml" in file_list:
                    toml_content = jar.read("META-INF/mods.toml").decode('utf-8', errors='ignore');
                    
                    # mods.toml - id
                    id_match = re.search(r'modId\s*=\s*"([^"]+)"', toml_content);
                    mod_id = id_match.group(1) if id_match else "Unknown";

                    # 3a.neoforge
                    if re.search(r'modId\s*=\s*"neoforge"', toml_content) or "NeoForge" in toml_content:
                        data_2 = {"type": "NeoForge", "id": mod_id, "jar_path": jar_path};
                        write_json_append(data_2, "mod_data.json");
                        print(f"[NeoForge] 文件: {jar_path} - ID: {mod_id}");
                        continue;
                    
                    # 3b.Forge
                    data_2 = {"type": "Forge", "id": mod_id, "jar_path": jar_path};
                    write_json_append(data_2, "mod_data.json");
                    print(f"[Forge] 文件: {jar_path} - ID: {mod_id}");
                    continue;
                
                print(f"[Unknown] 文件: {jar_path}");

        except zipfile.BadZipFile:
            data_2 = {"type": "Error", "id": "损坏的压缩包", "jar_path": jar_path};
            write_json_append(data_2, "mod_data.json");
            print(f"[Error] {jar_path} - 损坏的压缩包");
        except Exception as e:
            data_2 = {"type": "Error", "id": str(e), "jar_path": jar_path};
            write_json_append(data_2, "mod_data.json");
            print(f"[Error] {jar_path} - {str(e)}");

#========================================#