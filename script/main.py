#coding=utf-8

import LoadStruct as ls
import Struct

if __name__ == "__main__":
    print("Start program...")
    path = "../sample.yml"
    loadStruct = ls.LoadStruct(path)
    # get struct
    struct = loadStruct.get_struct()
    # show data
    struct.print_struct()
    pass