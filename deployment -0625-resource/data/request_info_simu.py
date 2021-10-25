# -*- coding: utf-8 -*-
import copy
import random

Q_filename = 'request_info_30.csv'
MS_filename = 'MS_info.csv'
# MSlist = ['a','b','c','d','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']    # 16个
MSlist = ['svc_a', 'svc_b', 'svc_c', 'svc_d', 'svc_e', 'svc_f', 'svc_g', 'svc_h', \
          'svc_i', 'svc_j', 'svc_k', 'svc_l', 'svc_m', 'svc_n', 'svc_o', 'svc_p']
Mslist = copy.deepcopy(MSlist[0:8])
Q_num = 30


def ms_chain(list, len):
    chain = copy.deepcopy(random.sample(list, len))
    chain.sort()
    return chain

def Q_info(mslist, q_num):
    q_list = []
    for i in range(q_num):
        list_line = []
        q_length = random.randint(1, len(mslist))
        mschain = ms_chain(mslist, q_length)
        list_line.extend([i, q_length, mschain])
        q_list.append(list_line)
    return q_list

Q_inf = Q_info(Mslist, Q_num)


def text_save(filename, data):              #filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'w')
    for i in range(len(data)):
        s = str(data[i])
        s = str(data[i]).replace('[','').replace(']','')    #去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'         #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print('保存文件' + filename + '成功')


def Q_file(filename, mslist, q_num):
    text_save(filename, Q_info(mslist, q_num))
# def N_file(filename, s_list):
#     text_save(filename, N_data(s_list))


Q_file(Q_filename, Mslist, Q_num)
# N_file(N_filename, slist)