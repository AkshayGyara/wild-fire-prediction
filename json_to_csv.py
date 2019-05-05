import numpy as np
import pandas as pd
import json
from ast import literal_eval
from pandas.io.json import json_normalize
import os

def json2xml(json_obj,line_padding=""):
    result_list = list()
    json_obj_type = type(json_obj)

    if json_obj_type is list:
        for sub_elem in json_obj:
            result_list.append(json2xml(sub_elem, line_padding))
        return "\n".join(result_list)

    if json_obj_type is dict:
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            result_list.append("%s<%s>" % (line_padding, tag_name))
            result_list.append(json2xml(sub_obj, "\t" + line_padding))
            result_list.append("%s</%s>" % (line_padding, tag_name))
        return "\n".join(result_list)
                
    return "%s%s" % (line_padding, json_obj)


rootdir = "/Users/nasrajan/Projects/SJSU/257/project/fire-prediction/data/Nitya/"
xmldir="/Users/nasrajan/Projects/SJSU/257/project/fire-prediction/data/Nitya_xml/"
directoryjson = os.fsencode(rootdir)

for file in os.listdir(directoryjson):
         filename = rootdir+str(os.fsdecode(file))
         print(filename)
         name=str(os.fsdecode(file))
         x=name.replace("json","xml")
         directoryxml = os.path.join(xmldir,x)
         
         if not os.path.exists(xmldir):
                os.makedirs(xmldir)
         f = open(directoryxml, "w")
         
         with open(filename) as json_data:
               data = json.load(json_data)
               f.write(str(json2xml(data)))
                
