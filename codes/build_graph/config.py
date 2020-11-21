#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:   Xukun Luo
# Date:     2020.11.18

DISH_URL = "http://162.105.89.218:22474"
DISH_USER = "neo4j"
DISH_PASSWORD = "python"
DISH_BOLT_PORT = 22090

SHICAI_PATH = "../../data/shicai/meishichina.txt"
CAIPIN_PATH = ["../../data/caipin/processing", "../../data/caipin/processing2"]
#CAIPIN_PATH = ["../../../data/processing", "../../../data/processing2"]

# Some attributes in CAIPIN
CAIPIN_ATTRS = {
    "名称": "", "别名": "", "步骤": "", "耗时": "", "难度": ""
}
CAIPIN_RELAS = {
    "菜系": ("菜品-菜系-属于", {}, "菜系"),
    "口味": ("菜品-口味-属于", {}, "口味"),
    "所属分类": ("菜品-菜品类-属于", {}, "菜品类"),
    "原材料": ("菜品-食材-包含", {"用量": ""}, "食材"),
    "适合人群": ("菜品-人群-适合", {"是否适合": ""}, "人群"),
    "工艺": ("菜品-工艺-使用", {}, "工艺")
}

""" Some definition """
CAIXI = [
    "川菜", "湘菜", "粤菜", "东北菜", "鲁菜", "浙菜", "苏菜", 
    "清真菜", "闽菜", "沪菜", "京菜", "湖北菜", "徽菜", "豫菜", 
    "西北菜", "云贵菜", "江西菜", "山西菜", "广西菜", "港台菜", "其它菜"
]
KOUWEI = [
    "酸", "甜", "苦", "辣", "咸", "鲜", "臭", "香", "咖喱", "糖醋", "蒜香"
]
CAIPINLEI = [
    "主食", "甜品", "热菜", "凉菜", "汤羹", "小吃", "西餐", 
    "烘焙", "饮品", "早餐", "中餐", "晚餐", "夜宵"
]
RENQUN = [
    "孕妇", "老人", "产妇", "哺乳期", "青少年", "幼儿", "学龄期儿童"
]
GONGYI = [
    "煎", "蒸", "炖", "红烧", "炸", "卤", "干锅", "火锅", "拌", "炒", "煮"
]
OTHERS = {
    "菜系": CAIXI, 
    "口味": KOUWEI, 
    "菜品类": CAIPINLEI, 
    "人群": RENQUN, 
    "工艺": GONGYI
}