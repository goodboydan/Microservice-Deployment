# -*- coding: utf-8 -*-
import random
import json


filename = "./node_info.json"
Node_list = ['node_A', 'node_B', 'node_C', 'node_D', 'node_E', 'node_F', 'node_G', 'node_H']
cpu_list = [1, 2, 3, 4]
# cpu_list = [2, 4, 6, 8]
mem_list = [1*1024, 2*1024, 3*1024, 4*1024]
# mem_list = [2*1024, 4*1024, 6*1024, 8*1024]


node_info_dict = {}
for node_name in Node_list:
    index = random.randint(0, 3)
    cpu = cpu_list[index]
    mem = mem_list[index]
    resource = [cpu, mem]
    node_info_dict[node_name] = [round(i,4) for i in resource]


with open(filename, 'w') as write_f:
	json.dump(node_info_dict, write_f, indent=4, ensure_ascii=False)