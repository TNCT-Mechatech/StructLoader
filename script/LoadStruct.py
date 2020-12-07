#encoding=utf-8
# File: LoadStructClass
# Discription: you are able to get struct class(struct_name,msg_id(int),List<Pair<variable_name,variable_type>>) 
# Date: 2020/12/6
# Author: testusuke
# GitHub: https://github.com/testusuke

class LoadStructClass:
    path = ""

    def __init__(self,path):
        print("init load struct list ")
        self.path = path
        sc = StructClass("",1)
        return sc
