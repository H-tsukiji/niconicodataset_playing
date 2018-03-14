# -*- coding:utf-8 -*-
import jsonlines

search_index = ["VOCALOID","初音ミク"]
read_file = "../niconico_moviedata.jsonl"

with jsonlines.open(read_file) as reader:
    for files in reader:
        tags = files["tags"]
        video_id = files["video_id"]
        flag = 0
        for search_word in search_index:
            if search_word in tags:
                flag = flag +1
        if flag >= 1:
            print(video_id)