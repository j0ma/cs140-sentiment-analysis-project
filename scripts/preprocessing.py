from collections import defaultdict
import json
from nltk import word_tokenize
# import emoji
import regex as re
# video title and comment time
# candidate,video_id,video_date,video_title,date,author,comment


def data_preprocessing(file, start):
    with open(file) as f:
        lines = f.readlines()
        # {video id1:{author1: comment, author2: comment2, author3: comment3, ... },
        #  video id2:{author1: comment, author2: comment2, author3: comment3, ... },...}
        dataset = defaultdict(lambda: defaultdict(str))
        skip_first_line = True
        video_id, author = 0, ''
        for line in lines:
            if skip_first_line:
                skip_first_line = False
                continue
            if line.startswith(start):
                tmp = line.split(',')
                video_id = 'video id: ' + tmp[1]

                video_title = ' video title: ' + tmp[3]

                comment_time = 'comment time: ' + tmp[4]
                author = tmp[5]

                comment = ' '.join(tmp[6:]).replace('\n', ' ') if tmp[6:] else ''
                dataset[video_id + video_title][author] = comment_time + ' ' + clean_comment(comment)
            else:
                line = line.replace('\n',' ')
                dataset[video_id + video_title][author] += ' '+clean_comment(line)

    json_file = './data/' + start[:-1] + '_preprocessed.json'
    write_json(json_file, dataset)


def clean_comment(comment):
    # print('\u201c' in comment)  # "
    # print('\u201d' in comment)  # "
    # print('\u2019' in comment)  # '
    # print('\u2026' in comment)  # ...
    comment = comment.replace('\u201c', '\"')
    comment = comment.replace('\u201d', '\"')
    comment = comment.replace('\u2019', '\'')
    comment = comment.replace('\u2026', ' ')
    # clean emoji unicode
    comment = (comment.encode('ascii', 'ignore')).decode("utf-8")
    return ' '.join([w.lower() for w in word_tokenize(comment)])

def write_json(json_file, dataset):
    with open(json_file, 'w') as f:
        json.dump(dataset, f)


# def extract_emojis(str):
#     emoji_list = []
#     data = regex.findall(r'\X', str)
#     for word in data:
#         if any(char in emoji.UNICODE_EMOJI for char in word):
#             emoji_list.append(word)
#
#     return emoji_list


if __name__ == "__main__":

    biden_file = './data/biden.csv'
    buttigieg_file = './data/buttigieg.csv'
    sanders_file = './data/sanders.csv'
    warren_file = './data/warren.csv'
    yang_file = './data/yang.csv'

    data_preprocessing(biden_file, 'biden,')
    data_preprocessing(buttigieg_file, 'buttigieg,')
    data_preprocessing(sanders_file, 'sanders,')
    data_preprocessing(warren_file, 'warren,')
    data_preprocessing(yang_file, 'yang,')
