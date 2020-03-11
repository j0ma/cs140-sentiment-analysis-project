import helpers as h
import pandas as pd
from collections import defaultdict

print('Extracting all comments...')
output = []

# let's iterate over the JSON file

for candidate_name, quarters in h.comments_dataset.items():
    for quarter, videos in quarters.items():
        for video in videos:
            video_id = video['id']
            video_title = video['title']
            video_comments = video['comments']
            comment_triplets = h.triplets(video_comments)
            for comment, date, author in comment_triplets:

                # gather all the infromation of this row into one dict
                d = {
                    'candidate': candidate_name,
                    'video_id': video_id,
                    'video_title': video_title,
                    'date': date,
                    'author': author,
                    'comment': comment
                }

                # strip away unnecessary whitespace
                for k, v in d.items():
                    d[k] = v.strip()

                output.append(d)

print('Creating DataFrame and saving to disk...')
all_comments = pd.DataFrame.from_records(output)
all_comments.to_csv('./data/all_comments.csv', index=False, encoding='utf-8', line_terminator='\n')

print('Separating into candidate-specific data frames and saving to disk...')
for candidate_name in all_comments.candidate.unique():
    out = all_comments[all_comments.candidate==candidate_name].copy()
    out.to_csv(f'./data/{candidate_name}.csv', index=False, encoding='utf-8', line_terminator='\n')
