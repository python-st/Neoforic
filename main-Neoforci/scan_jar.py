# -*- coding : utf-8 -*-

# scan_jar.py

#========================================#

#import

import glob;
import zipfile;
import re;
import os;
from write_json import write_json_append , read_json;
from print_log import w_log;
from setup import mods_dir;

w_log("scan_log", "INFO", "scan_jar.py启动 √ ");

#========================================#


if not os.path.exists(mods_dir()):
    os.makedirs(mods_dir());
else:
    jar_files = glob.glob(os.path.join(mods_dir(), "*.jar"));

#========================================#

#code

class NeoforciScanner:
    # Neoforci 扫描内核

    def __init__ (self):

        if os.path.exists("mod_data.json"):

            os.remove("mod_data.json");
            w_log("scan_log", "INFO", "清理旧的 mod_data.json √ ");

        w_log("scan_log", "INFO", "【Neoforci 扫描内核】已启动");

    @staticmethod
    def scan():

        w_log("scan_log", "INFO", "开始执行 jar 文件扫描任务...");

        for jar_path in jar_files:

            try:

                with zipfile.ZipFile(jar_path, "r") as jar:

                    file_list = jar.namelist();

                    # 1.Fabric
                    if "fabric.mod.json" in file_list:

                        content = jar.read("fabric.mod.json").decode("utf-8", errors='ignore');
                        id_match = re.search(r'"id"\s*:\s*"([^"]+)"', content);
                        mod_id = id_match.group(1) if id_match else "Unknown";
                        data_2 = {"type": "Fabric", "id": mod_id, "jar_path": jar_path};
                        write_json_append(data_2);
                        w_log("scan_log", "INFO", f"[Fabric] 文件: {jar_path} - ID: {mod_id}");
                        continue;

                    # 2.NeoForge
                    elif "META-INF/neoforge.mods.toml" in file_list:

                        content = jar.read("META-INF/neoforge.mods.toml").decode('utf-8', errors='ignore');
                        id_match = re.search(r'modId\s*=\s*"([^"]+)"', content);
                        mod_id = id_match.group(1) if id_match else "Unknown";
                        data_2 = {"type": "NeoForge", "id": mod_id, "jar_path": jar_path};
                        write_json_append(data_2, "mod_data.json");
                        w_log("scan_log", "INFO", f"[NeoForge] 文件: {jar_path} - ID: {mod_id}");
                        continue;

                    elif "META-INF/mods.toml" in file_list:

                        toml_content = jar.read("META-INF/mods.toml").decode('utf-8', errors='ignore');
                        id_match = re.search(r'modId\s*=\s*"([^"]+)"', toml_content);
                        mod_id = id_match.group(1) if id_match else "Unknown";
                        
                        # 3a.neoforge
                        if re.search(r'modId\s*=\s*"neoforge"', toml_content) or "NeoForge" in toml_content:

                            data_2 = {"type": "NeoForge", "id": mod_id, "jar_path": jar_path};
                            write_json_append(data_2, "mod_data.json");
                            w_log("scan_log", "INFO", f"[NeoForge] 文件: {jar_path} - ID: {mod_id}");
                            continue;
                                            
                        # 3b.Forge
                        else:

                            data_2 = {"type": "Forge", "id": mod_id, "jar_path": jar_path};
                            write_json_append(data_2, "mod_data.json");
                            w_log("scan_log", "INFO", f"[Forge] 文件: {jar_path} - ID: {mod_id}");
                            continue;
                    
                    if "META-INF/MANIFEST.MF" in file_list:

                        manifest_content = jar.read("META-INF/MANIFEST.MF").decode('utf-8', errors='ignore');

                        if "FML" in manifest_content and "neoforge" in manifest_content:
                                
                                data_2 = {"type": "NeoForge", "id": "Unknown", "jar_path": jar_path};
                                write_json_append(data_2, "mod_data.json");
                                w_log("scan_log", "INFO", f"[NeoForge] 文件: {jar_path} - ID: Unknown");
                                continue;
                        
                        else:

                            data_2 = {"type": "Forge", "id": "Unknown", "jar_path": jar_path};
                            write_json_append(data_2, "mod_data.json");
                            w_log("scan_log", "INFO", f"[Forge] 文件: {jar_path} - ID: Unknown");
                            continue;

                    w_log("scan_log", "WARNING", f"[Unknown] 文件: {jar_path}");

            except zipfile.BadZipFile:

                data_2 = {"type": "Error", "id": "损坏的压缩包", "jar_path": jar_path};
                write_json_append(data_2, "mod_data.json");
                w_log("scan_log", "ERROR", f"[Error] {jar_path} - 损坏的压缩包");
            except Exception as e:

                data_2 = {"type": "Error", "id": str(e), "jar_path": jar_path};
                write_json_append(data_2, "mod_data.json");
                w_log("scan_log", "ERROR", f"[Error] {jar_path} - {str(e)}");

        w_log("scan_log", "INFO", "jar 文件扫描任务完成 √ ");

    @staticmethod
    def ver():

        w_log("scan_log", "INFO", "开始执行 ver_jar 查重逻辑...");
        mod_dict = {};

        for mod in read_json():

            mod_id = mod["id"];

            if mod_id in mod_dict:

                w_log("scan_log", "WARNING", f"[重复] 文件: {mod['jar_path']} - ID: {mod_id}");
            
            else:

                mod_dict[mod_id] = mod;
            
        return list(mod_dict.values()); 

#========================================#

if __name__ == "__main__":
    print("怎么可能啊，绝对不可能。");
