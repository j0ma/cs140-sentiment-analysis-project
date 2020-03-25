import json
import jsonlines
def write_jsonline(json_file):
    with jsonlines.open("./data/sanders.jsonl",mode='w') as writer:
        with open(json_file) as f:
            data=json.load(f)
            for video in data:
                for author in data[video]:
                    comment=data[video][author]
                    dict={"text":video + "\n\n" + author + "\n\n" + comment}
                    writer.write(dict)


write_jsonline("./data/sanders_preprocessed.json")
