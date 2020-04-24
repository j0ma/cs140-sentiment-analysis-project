import json
import jsonlines

def write_jsonline(json_file):
    with jsonlines.open("./data/yang.jsonl",mode='w') as writer:
        with open(json_file) as f:
            data=json.load(f)
            for video in data:
                for author in data[video]:
                    comment=data[video][author]
                    dict={"text":video + " author: " + author + " " + comment}
                    writer.write(dict)

def write_jsonline_new(input_file, output_file):
    with jsonlines.open(output_file, 'w') as writer:
        with open(input_file) as f:
            data = json.load(f)
            for ix, row in data.items():
                writer.write(row)

if __name__ == '__main__':
    #write_jsonline("./data/yang_preprocessed.json")
    write_jsonline_new(input_file="./data/biden.test.json", 
                       output_file="./data/biden.test.jsonl")
