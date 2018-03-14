# -*- coding:utf-8 -*-
import jsonlines
import numpy as np

read_file = "../test_data.jsonl"
tag_index = []
count = 1

#タグインデックス読み込み
f = open("testread.txt","r")
for line in f:
    line = line.replace('\n','')
    tag_index.append(line)

tag_vac = np.ones(len(tag_index))
#tagベクトルの作成
with jsonlines.open(read_file) as reader:
    for files in reader:
        print(count)
        movie_tag = np.zeros(len(tag_index))
        for tag in files["tags"]:
            if tag in tag_index:
                continue
            else:
                tag_index.append(tag)
        count = count + 1

'''
hoge = [0,0,1,1,1]
ho = np.array(hoge)
print(hoge)


## numpy.vstack() で行方向に結合
>>> np.vstack((a,b))
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8],
       [8, 7, 6],
       [5, 4, 3],
       [2, 1, 0]])
'''