# -*- coding:utf-8 -*-
import jsonlines,csv
import numpy as np

read_file = "../test_data.jsonl"
tag_index = []
count = 1

#タグインデックス読み込み
f = open("testread.txt","r",encoding="utf-8")
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
                index_num = tag_index.index(tag)
                movie_tag[index_num] = 1
            else:
                continue
        tag_vac = np.vstack((tag_vac,movie_tag))
        count = count + 1
tag_vac = np.delete(tag_vac,0,0)


print(tag_vac)

'''
write_file = open("../testvsctor.csv","w",encoding="utf-8")
for line in tag_index:
    for score in tag_index[line]:
        write_file.write(str(score)+",")
    write_file.write("\n")
'''

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