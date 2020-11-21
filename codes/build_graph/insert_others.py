#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:   Xukun Luo
# Date:     2020.11.21

import sys
from tqdm import tqdm
sys.path.append('../../')

from codes.build_graph.GraphController import DishController
from codes.build_graph.config import DISH_URL, DISH_USER, DISH_PASSWORD, DISH_BOLT_PORT
from codes.build_graph.config import OTHERS, CAIXI, KOUWEI, CAIPINLEI, RENQUN, GONGYI

def insert_others():
    dish_controller = DishController(DISH_URL, DISH_USER, DISH_PASSWORD, DISH_BOLT_PORT)

    for key, value in OTHERS.items():
        for node_name in value:
            node = dish_controller.insertNode(key, {"名称": node_name})

    print("Insert others successfully!")

if __name__ == "__main__":
    insert_others()