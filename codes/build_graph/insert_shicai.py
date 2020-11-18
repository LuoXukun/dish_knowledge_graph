#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:   Xukun Luo
# Date:     2020.11.18

import sys
from tqdm import tqdm
sys.path.append('../../')

from codes.build_graph.GraphController import DishController
from codes.build_graph.config import DISH_URL, DISH_USER, DISH_PASSWORD, DISH_BOLT_PORT, SHICAI_PATH

def insert_shicai():
    dish_controller = DishController(DISH_URL, DISH_USER, DISH_PASSWORD, DISH_BOLT_PORT)
    
    shicai_lei, shicai = [], []

    # Load the shicai lei in.
    with open(SHICAI_PATH, "r", encoding="utf-8") as f:
        for idx, text in enumerate(f):
            text = text.strip().split(":")
            if len(text) < 2: continue
            shicai_lei.append(text[0].strip())
            shicai.append(text[-1].split(",")[:-1])
            assert len(shicai_lei) == len(shicai)
    
    # Insert the node and relations
    for idx in tqdm(range(len(shicai_lei))):
        shicai_lei_node = dish_controller.insertNode("食材类别", {"名称": shicai_lei[idx]})
        for item in shicai[idx]:
            shicai_node = dish_controller.insertNode("食材", {"名称": item, "有无特殊气味": "NULL"})
            # Insert the relation
            dish_controller.insertRelation("食材-食材类别-属于", "食材", "食材类别", item, shicai_lei[idx], {})

    print("Insert shicai successfully!")

if __name__ == "__main__":
    insert_shicai()