# -*- coding: utf-8 -*-
import random
import json

filename = "./svc_info.json"
MSlist = ['svc_a', 'svc_b', 'svc_c', 'svc_d', \
          'svc_e', 'svc_f', 'svc_g', 'svc_h', \
          'svc_i', 'svc_j', 'svc_k', 'svc_l', \
          'svc_m', 'svc_n', 'svc_o', 'svc_p']
# image_version = ['Ubuntu', 'CentOS', 'Debian']
Image_version = ['BusyBox', 'Alpine','Ubuntu', 'CentOS', 'Debian', 'Fedora']
Version_coefficient = {'BusyBox':0.2, 'Alpine':0.15,'Ubuntu':1, 'CentOS':0.9, 'Debian':0.85, 'Fedora':0.8}
cpu_cardinality = [random.uniform(0.01, 0.25) for i in range(len(MSlist))]
mem_cardinality = [random.uniform(16, 256) for i in range(len(MSlist))]
load_cardinality = [random.uniform(0.1, 10) for i in range(len(MSlist))]
error_rate_cardinality = [random.uniform(0.01, 0.1) for i in range(len(MSlist))]

svc_info_dict = {}
for svc_item in MSlist:
    index = MSlist.index(svc_item)
    cardinality = [cpu_cardinality[index], mem_cardinality[index], load_cardinality[index], error_rate_cardinality[index]]
    single_svc_info = {}
    for version in Image_version:
        svc_version_info = {}
        coef = Version_coefficient[version]
        svc_version_info['cpu'] = round(random.uniform(coef-0.1, coef+0.1) * cardinality[0], 4)
        svc_version_info['mem'] = round(random.uniform(coef-0.1, coef+0.1) * cardinality[1], 4)
        svc_version_info['load'] = round(random.uniform(coef-0.1, coef+0.1) * cardinality[2], 4)
        svc_version_info['error_rate'] = round(random.uniform(0.9, 1) * cardinality[3], 4)
        svc_version_info['deploy_num'] = 0
        single_svc_info[version] = svc_version_info
    svc_info_dict[svc_item] = single_svc_info


with open(filename, 'w') as write_f:
	json.dump(svc_info_dict, write_f, indent=4, ensure_ascii=False)

