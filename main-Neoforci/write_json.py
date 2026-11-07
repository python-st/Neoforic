# -*- coding : utf-8 -*-

#========================================#

#import

import json;
import os;

#========================================#

#code

def write_json_append(data, filename):
    existing_data = [];
    
    # read
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            try:
                existing_data = json.load(f);

                if isinstance(existing_data, dict):
                    existing_data = [existing_data];
            except json.JSONDecodeError:
                existing_data = [];

    # 加入
    if isinstance(data, list):
        existing_data.extend(data);
    else:
        existing_data.append(data);

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4);

#========================================#

if __name__ == "__main__":
    #怎么可能啊，绝对不可能。
    print("怎么可能啊，绝对不可能。");