# -*- coding:utf-8 -*-
import jsonlines

with jsonlines.open('0168.jsonl') as reader:
    for files in reader:
        tags = files["tags"]
        video_id = files["video_id"]
        watch_num = files["watch_num"]
        comment_num = files["comment_num"]
        mylist_num = files["mylist_num"]
        title = files["title"]
        description = files["description"]
        category = files["category"]
        tag_index = files["tags"]
        upload_time = files["upload_time"]
        file_type = files["file_type"]
        length = files["length"]
        size_high = files["size_high"]
        size_low = files["size_low"]
        print(video_id)