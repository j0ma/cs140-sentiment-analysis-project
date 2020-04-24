import json
import jsonlines
import helpers as h

CANDIDATES = set(['biden', 'yang', 'buttigieg', 'warren', 'sanders'])

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

    for cand in CANDIDATES:
        print(f'Processing data for: {cand}')
        input_file = f"./data/{cand}_preprocessed.json"
        output_file = f"./data/{cand}.jsonl"
        write_jsonline_new(input_file=input_file,
                           output_file=output_file)
