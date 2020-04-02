from flask import Flask, render_template, request, make_response, redirect, jsonify
import json

app = Flask(__name__)

ACTIVE_DATASET = None
VIDS = None

@app.route('/get_comment')
def get_comment():
    vid_index = int(request.args.get('vid_index'))
    comment_index = int(request.args.get('comment_index'))

    vid = VIDS[vid_index]
    comments = list(ACTIVE_DATASET[vid].values())
    comment = comments[comment_index]

    try:
        next_vid_index = vid_index
        next_comment_index = comment_index+1
        temp = VIDS[vid_index]
        comments = list(ACTIVE_DATASET[vid].values())
        temp = comments[comment_index]
    except:
        next_vid_index = vid_index + 1
        next_comment_index = 0

    return json.dumps([vid, comment, next_vid_index, next_comment_index])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_upload', methods=['GET'])
def check_upload():
    return jsonify(ACTIVE_DATASET)

@app.route('/upload', methods=['POST'])
def upload():
    global ACTIVE_DATASET
    global VIDS
    ACTIVE_DATASET = json.loads(request.files["annotate_this"].read())
    VIDS = list(ACTIVE_DATASET.keys())
    print('Active dataset from inside /upload')
    # print(ACTIVE_DATASET)
    return redirect('/annotate')

@app.route('/annotate/<vid_index>/<comment_index>')
def annotate(vid_index, comment_index):
    return render_template('annotation.html', vid=vid_index, comment=comment_index)

@app.route('/annotate')
def start_annotate():
    with open('indices.txt') as index_doc:
        indices = json.load(index_doc)
        vid_index = indices['video']
        comment_index = indices['comment']
    return redirect('annotate/{}/{}'.format(vid_index, comment_index))

@app.route('/submit', methods=['POST'])
def submit():
    aspects = json.loads(request.form.get('aspects'))
    comment = request.form.get('comment')
    vid_index = request.form.get('next_vid_index')
    comment_index = request.form.get('next_comment_index')
    with open('annotations.jsonl', 'a') as outfile:
        outfile.write(json.dumps({'comment': comment, 'aspects': aspects})+'\n')
    
    with open('indices.txt', 'w') as index_doc:
        json.dump({'video': vid_index, 'comment':comment_index}, index_doc)

    return ''

@app.route('/results')
def results():
    with open('annotations.jsonl') as results_file:
        resp = make_response(results_file.read(), 200)
        resp.mimetype = "text/plain"
        return resp

if __name__ == "__main__":
    app.run(debug=True)
