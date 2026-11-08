# -*- coding : utf-8 -*-

#========================================#

#import

import json;
import os;

#========================================#

#code

def write_json_append(data, filename):

    if not os.path.exists(filename):

        existing_data = [];

    else:

        try:

            with open(filename, 'r', encoding='utf-8') as f:

                existing_data = json.load(f);
                if not isinstance(existing_data, list):

                    existing_data = [existing_data];

        except json.JSONDecodeError:
            existing_data = [];

    if isinstance(data, list):

        existing_data.extend(data);
    
    else:

        existing_data.append(data);

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4);

def read_json():
    
    if not os.path.exists("mod_data.json"):
        return 404;
    else:
        with open("mod_data.json", 'r', encoding="utf-8") as f:
            data = json.load(f);
            return data;
            

#========================================#

if __name__ == "__main__":
    #怎么可能啊，绝对不可能。
    print("怎么可能啊，绝对不可能。");