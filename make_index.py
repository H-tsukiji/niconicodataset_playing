# -*- coding:utf-8 -*-
import jsonlines
import numpy as np

read_file = "../test_data.jsonl"
tag_index = []
word_num = {}
count = 1

#すべてのタグの索引を作る
with jsonlines.open(read_file) as reader:
    for files in reader:
        print(count)
        for tag in files["tags"]:
            if tag in tag_index:
                word_num[tag] += 1
            else:
                tag_index.append(tag)
                word_num[tag] = 1
        count = count + 1


#一回だけの奴はけす
for key in list(word_num):
    if word_num[key] == 1:
        del(word_num[key])
result_index = word_num.keys()

f = open('test_read.txt', 'w', encoding="utf-8")
for x in result_index:
    f.write(x + "\n")
f.close()