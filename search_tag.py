import jsonlines

with jsonlines.open('0168.jsonl') as reader:
    for files in reader:
        tags = files["tags"]
        video_id = files["video_id"]
        if "VOCALOID" in tags:
            print (video_id)