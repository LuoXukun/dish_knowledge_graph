#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:   Xukun Luo
# Date:     2020.11.18

from py2neo import Graph, Node, Relationship, NodeSelector

# 与菜品图数据库的交互类
class DishController(object):
    # 初始化函数
    """ 
        url: neo4j数据库的地址
        user: 数据库用户名
        password: 数据库密码
        bolt_port: 数据库接入端口
    """
    def __init__(self, url, user, password, bolt_port):
        self.url = url
        self.user = user
        self.password = password
        self.bolt_port = bolt_port
        self.graph = Graph(self.url, user=self.user, password=self.password, bolt_port=self.bolt_port)
    
    # 往数据库中插入节点
    """ 
        node_type: 节点类型
        attribute: 节点附带属性
    """
    def insertNode(self, node_type, attribute):
        node_selector = NodeSelector(self.graph)
        drug_node = node_selector.select(node_type, 名称=attribute["名称"]).first()
        if drug_node == None:
            drug_node = Node(node_type)
            drug_node["名称"] = attribute["名称"]
            self.graph.create(drug_node)
        for key, value in attribute.items():
            drug_node[key] = value
        self.graph.push(drug_node)
        return drug_node
    
    # 往数据库中插入关系
    """ 
        relation_name: 关系类型
        type1: 节点1类型
        type2: 节点2类型
        name1: 节点1名称属性值
        name2: 节点2名称属性值
        attribute: 关系附带属性
    """
    def insertRelation(self, relation_name, type1, type2, name1, name2, attribute):
        # 先将节点插入数据库
        node1 = self.insertNode(type1, {"名称": name1})
        node2 = self.insertNode(type2, {"名称": name2})
        # 插入两个节点间的关系
        rel_match = self.graph.match(rel_type=relation_name, start_node=node1, end_node=node2, bidirectional=True)
        if len(list(rel_match)) == 0:
            rel_match = Relationship(node1, relation_name, node2)
            self.graph.create(rel_match)
        for key, value in attribute.items():
            rel_match[key] = value
        self.graph.push(rel_match)
        return rel_match

if __name__ == "__main__":
    pass