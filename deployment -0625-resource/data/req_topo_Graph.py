# -*- coding: utf-8 -*-
import random
import os
import csv


filename_req = "./request_info_30.csv"
filename_svc = "./svc_info.json"
filename_req_topo = "./req_topo_info_30.csv"


def read_reqlist(file):
    rs = os.path.exists(file)
    if rs == True:
        f = open(file, 'r', encoding='utf-8')
        list_req = []
        csvreader = csv.reader(f)
        list_tmp = list(csvreader)
        for line in list_tmp:
            line = line[0].split(" ")
            line[0] = int(line[0])
            line[1] = int(line[1])
            list_req.append(line)
    return list_req


def prob_value(p):                      # 一个按概率连边的函数
    q = int(10*p)
    l = [1]*q+[0]*(10-q)
    item = random.sample(l,1)[0]        # random.sample输出是list，加上元素位置后才是int
    return item


def text_save(filename, data):          # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'w')
    for i in range(len(data)):
        s = str(data[i])
        s = str(data[i]).replace('[','').replace(']','')    # 去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace('),',')') +'\n'       # 去除单引号，非必要的逗号，每行末尾追加换行符
        s = s.replace(', ', ',')
        s = s.replace('(', '').replace(')', '')
        # s = s.replace('(', '[').replace(')', ']').replace(', ', ',')
        file.write(s)
    file.close()
    print('保存文件' + filename + '成功')


def make_one_graph(chain_len):
    n = chain_len
    into_degree = [0]*n                     # 节点入度列表
    out_degree = [0]*n                      # 节点出度列表
    edges = []                              # 存储边的列表

    # 拓扑序就按[1,n]的顺序，依次遍历加边
    for i in range(n-1):
        for j in range(i+1,n):
            if i==0 and j==n-1:             # 不直连入口和出口
                continue
            prob = prob_value(0.4)          # 连边的概率取0.4
            if prob:
                if out_degree[i]<2 and into_degree[j]<2:    # 限制节点的入度和出度不大于2
                    edges.append((i,j))     # 连边
                    into_degree[j]+=1
                    out_degree[i]+=1
    for node,id in enumerate(into_degree):  # 给所有没有入边的节点添加入口节点作父亲
        if node!=0:
            if id ==0:
                edges.append((0,node))
                out_degree[0]+=1
                into_degree[node]+=1
    for node,od in enumerate(out_degree):   # 给所有没有出边的节点添加出口节点作儿子
        if node!=n-1:
            if od ==0:
                edges.append((node,n-1))
                out_degree[node] += 1
                into_degree[n-1]+=1
    return edges, into_degree, out_degree


def trans_index_to_svc(edgelist_index, list_ms_line):
    edgelist_svc = []
    for edge in edgelist_index:
        edgelist_svc.append((list_ms_line[edge[0]], list_ms_line[edge[1]]))
    return edgelist_svc


reqs_topo_list = []
for req in read_reqlist(filename_req):
    single_topo_edges, _, _ = make_one_graph(req[1])
    single_topo_edges.sort()
    reqs_topo_list.append(single_topo_edges)
# text_save(filename_req_topo, reqs_topo_list)

ms_list = read_reqlist(filename_req)
for i in range(len(ms_list)):
    ms_list[i] = ms_list[i][2:]
topo_list = []
for i in range(len(reqs_topo_list)):
    topo_list.append(trans_index_to_svc(reqs_topo_list[i], ms_list[i]))

text_save(filename_req_topo, topo_list)
