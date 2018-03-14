# -*- coding:utf-8 -*-
import os,jsonlines
from glob import glob

read_dir  = "D:/niconico_dataset/movie_metadata"
out_dir = "niconico_moviedata.jsonl"

files = glob(os.path.join(read_dir, '*.jsonl'))
for file in files:
    print(file)
    with jsonlines.open(file) as reader:
        for metadata in reader:
            with jsonlines.open(out_dir, mode='a') as writer:
                writer.write(metadata)