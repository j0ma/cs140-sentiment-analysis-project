from flask import Flask, render_template, request, make_response, redirect, jsonify
import json

app = Flask(__name__)

ACTIVE_DATASET = None

with open('../data/buttigieg_preprocessed.json') as f:
    j = json.load(f)
    vids = list(j.keys())

def get_comment():
    with open('indices.txt') as index_doc:
        indices = json.load(index_doc)
        vid_index = indices['video']
        comment_index = indices['comment']

    try:
        vid = vids[vid_index]
        comments = list(j[vid].values())
        comment = comments[comment_index]
    except:
        vid_index += 1
        comment_index = 0
        vid = vids[vid_index]
        comments = list(j[vid].values())
        comment = comments[comment_index]

    with open('indices.txt', 'w') as index_doc:
        json.dump({'video': vid_index, 'comment':comment_index+1}, index_doc)

    return vid, comment

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_upload', methods=['GET'])
def check_upload():
    return jsonify(ACTIVE_DATASET)

@app.route('/upload', methods=['POST'])
def upload():
    global ACTIVE_DATASET
    ACTIVE_DATASET = json.loads(request.files["annotate_this"].read())
    print('Active dataset from inside /upload')
    print(ACTIVE_DATASET)
    return redirect('/annotate')

@app.route('/annotate')
def annotate():
    vid, comment = get_comment()
    return render_template('annotation.html', vid=vid, comment=comment)

@app.route('/submit', methods=['POST'])
def submit():
    aspects = list(set(json.loads(request.form.get('aspects'))))
    comment = request.form.get('comment')
    with open('annotations.jsonl', 'a') as outfile:
        outfile.write(json.dumps({'comment': comment, 'aspects': aspects})+'\n')
    next_vid, next_comment = get_comment()
    return json.dumps([next_vid, next_comment])

@app.route('/results')
def results():
    with open('annotations.jsonl') as results_file:
        resp = make_response(results_file.read(), 200)
        resp.mimetype = "text/plain"
        return resp

if __name__ == "__main__":
    app.run(debug=True)
