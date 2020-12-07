#encoding=utf-8
# File: LoadStruct
# Discription: you are able to get struct class(struct_name,msg_id(int),List<Pair<variable_name,variable_type>>) 
# Date: 2020/12/6
# Author: testusuke
# GitHub: https://github.com/testusuke

import Struct
import os
import traceback

class LoadStruct:
    def __init__(self,path):
        print("info: init LoadStruct")
        self.path = path
        # load struct
        self.load_struct()

        return self.struct
        
    def load_struct(self):
        print("info: loading file:" + self.path)
        # check exist file
        if not os.path.exists(self.path):
            try:
                raise ValueError("Error: fine not exist")
            except ValueError as e:
                traceback.print_exc()
        # check file type
        root, ext = os.path.splitext(self.path)
        if ext != '.yml':
            try:
                raise ValueError("Error: file is not yaml file")
            except ValueError as e:
                traceback.print_exc()
        
        # create instance
        self.struct = Struct(name,msg_id)
        # add variables