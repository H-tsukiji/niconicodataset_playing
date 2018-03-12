import os,jsonlines
from glob import glob

read_dir  = "file_connection"
out_dir = ""

files = glob(os.path.join(read_dir, '*.jsonl'))
for file in files:
    print(file)
    with jsonlines.open('0168.jsonl') as reader:
        for files in reader:
            tags = files["tags"]
            video_id = files["video_id"]
            flag = 0
            for search_word in search_index:
                if search_word in tags:
                    flag = flag +1
            if flag >= 1:
                print(video_id)