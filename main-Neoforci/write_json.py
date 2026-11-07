# -*- coding : utf-8 -*-

#========================================#

#import

import json;

#========================================#

#code

def write_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4);

#========================================#

if __name__ == "__main__":
    #怎么可能啊，绝对不可能。
    print("怎么可能啊，绝对不可能。");