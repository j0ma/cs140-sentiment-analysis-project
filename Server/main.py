from flask import Flask, render_template, request, make_response, redirect, jsonify
import json
import re

app = Flask(__name__)

ACTIVE_DATASET = None

@app.route('/get_comment')
def get_comment():
    comment_index = int(request.args.get('comment_index'))

    comment_parts = ACTIVE_DATASET[comment_index]

    # comment_parts = re.split(r"video id: | video title: | author: | comment time: .*? ", comment_parts)

    print('Comment parts')
    print(comment_parts)

    # video_title = comment_parts[2]
    # comment = comment_parts[4]

    video_title = comment_parts['video_title']
    comment = comment_parts['comment']

    next_comment_index = comment_index+1
    
    return json.dumps([video_title, comment, next_comment_index])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_upload', methods=['GET'])
def check_upload():
    return jsonify(ACTIVE_DATASET)

@app.route('/upload', methods=['POST'])
def upload():
    global ACTIVE_DATASET
    lines = request.files["annotate_this"].read()
    print(lines)
    lines = lines.decode('utf-8').split("\n")
    lines = [line for line in lines if line]
    #ACTIVE_DATASET = [json.loads(line).get('text') for line in lines]
    ACTIVE_DATASET = [json.loads(line) for line in lines]
    print(ACTIVE_DATASET[0])
    print('Active dataset from inside /upload')
    return redirect('/annotate')

@app.route('/annotate/<comment_index>')
def annotate(comment_index):
    return render_template('annotation.html', comment=comment_index)

@app.route('/annotate')
def start_annotate():
    try:
        with open('indices.txt') as index_doc:
            comment_index = int(index_doc.read().strip())
    except:
        comment_index = 0 
    return redirect('annotate/{}'.format(comment_index))

@app.route('/submit', methods=['POST'])
def submit():
    aspects = json.loads(request.form.get('aspects'))
    comment = request.form.get('comment')
    next_comment_index = request.form.get('next_comment_index')
    with open('annotations.jsonl', 'a') as outfile:
        outfile.write(json.dumps({'comment': comment, 'aspects': aspects})+'\n')
    
    with open('indices.txt', 'w') as index_doc:
        index_doc.write(next_comment_index)

    return ''

@app.route('/results')
def results():
    with open('annotations.jsonl') as results_file:
        resp = make_response(results_file.read(), 200)
        resp.mimetype = "text/plain"
        return resp

if __name__ == "__main__":
    app.run(debug=True)
