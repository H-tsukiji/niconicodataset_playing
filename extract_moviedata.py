# -*- coding:utf-8 -*-
import jsonlines

search_category = "VOCALOID"
read_file = "../niconico_moviedata.jsonl"
write_file = "../vocaloid_moviedata.jsonl"

with jsonlines.open(read_file) as reader:
    for files in reader:
        category = files["category"]
        if category == search_category:
            with jsonlines.open(write_file, mode='a') as writer:
                writer.write(files)