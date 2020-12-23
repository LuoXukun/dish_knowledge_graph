#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:   Xukun Luo
# Date:     2020.11.18

# 注意：将 data/caipin/ 下的两个压缩文件解压缩后再运行本程序

import sys
import os
import copy
import re
from tqdm import tqdm
sys.path.append('../../')

from codes.build_graph.GraphController import DishController
from codes.build_graph.config import DISH_URL, DISH_USER, DISH_PASSWORD, DISH_BOLT_PORT
from codes.build_graph.config import CAIPIN_PATH, CAIPIN_ATTRS, CAIPIN_RELAS, CAIPINLEI

def insert_caipin():

    dish_controller = DishController(DISH_URL, DISH_USER, DISH_PASSWORD, DISH_BOLT_PORT)

    for dir_path in CAIPIN_PATH:
        print(dir_path)
        file_name_list = os.listdir(dir_path)
        file_name_list.sort()
        #print(file_name_list[0])
        for idx, file_name in enumerate(file_name_list):
            if idx % 1000 == 0:
                print("Epoch: ", idx)
            with open(os.path.join(dir_path, file_name), "r", encoding="utf-8") as f:
                data = f.read().split('\n')
            
            # insert the caipin node
            caipin_attr = copy.copy(CAIPIN_ATTRS)
            for line in data:
                line = re.split(":|：", line.replace("菜名", "名称"))
                if len(line) != 2: continue
                key = line[0].strip()
                if key not in caipin_attr.keys(): continue
                value = line[1].strip().replace("。。。", "。")
                if key == "名称":
                    value = value.split("#")[-1].strip()
                caipin_attr[key] = value
            #print(caipin_attr)

            if caipin_attr["名称"]:
                caipin_node = dish_controller.insertNode("菜品", caipin_attr)
            else:
                continue

            # insert the relations
            for line in data:
                line = re.split(":|：", line)
                if len(line) != 2: continue
                key = line[0].strip()
                if key not in CAIPIN_RELAS.keys(): continue
                caipin_rela = copy.copy(CAIPIN_RELAS[key])
                value = re.split(" +", line[1].strip())
                if key == "原材料":
                    # 插入食材和菜品的关系
                    if len(value) % 2 != 0: continue
                    for i in range(0, len(value), 2):
                        caipin_rela[1]["用量"] = value[i+1].strip()
                        dish_controller.insertRelation(caipin_rela[0], "菜品", caipin_rela[2], caipin_attr["名称"], value[i].strip(), caipin_rela[1])
                elif key == "适用人群":
                    pass
                elif key == "所属分类":
                    # 插入菜品和所属类别的关系
                    for item in value:
                        tmp = item.strip()
                        if tmp == "": continue
                        if tmp not in CAIPINLEI: continue
                        dish_controller.insertRelation(caipin_rela[0], "菜品", caipin_rela[2], caipin_attr["名称"], tmp, caipin_rela[1])            
                else:
                    # 插入其他在文档中出现的关系
                    for item in value:
                        if item.strip() == "": continue
                        dish_controller.insertRelation(caipin_rela[0], "菜品", caipin_rela[2], caipin_attr["名称"], item.strip(), caipin_rela[1])

        print("Push successfully: {} !".format(dir_path))

if __name__ == "__main__":
    insert_caipin()