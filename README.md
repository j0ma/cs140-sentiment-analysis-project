# CS140 Sentiment Analysis Annotation Project

## Instructions for annotators

Hello, dear annotator! ( ͡° ͜ʖ ͡°)

This repository contains our code and data for the CS140 group project on sentiment analysis.

In `./data/comments_for_annotators` you will find 5 `jsonl` files, each corresponding to a 2020 presidential candidate.

Each file contains 200 comments, randomly sampled from the YouTube data set collected earlier in the semester.

Your mission, should you choose to accept it, is as follows:

0. Fork this repository under your own name.
1. Set up a Python 3 development environment, e.g. using `conda`.
2. Install dependencies by running `pip install -r requirements.txt`
3. Go to `./Server/` and run `python main.py`
4. In your web browser of choice, navigate to `https://localhost:5000`
5. Click `"Browse"`, navigate to `./data/comments_for_annotators`, and choose the file `<assigned_candidate>.200.jsonl`. Afterwards, click `"Upload"`.
6. Wait to be redirected and annotate.
    - If you need to revise an annotation, feel free to alter comment index in the URL to backward by your desired number of comments.
7. After annotating, your annotation file will be `./Server/annotations.jsonl`
8. Rename your annotation file by running `mv annotations.jsonl <candidate-last-name>-annotated-<your-name>.jsonl` where `<candidate-last-name>` should be replaced with a lowercased version of the candidate's name, e.g. `biden`, and `<your-name>` should be lowercased and hyphenated, e.g. `louis-brandeis`.
9. Submit your annotations by committing to your own version of the repository, and submit a pull reqeuest to the original repository.

Good luck!! (•̀ᴗ•́)൬༉

### Candidate-annotator assinments

Here is the schedule of candidate-annotator assignments:

| Candidate   |    Annotator                |
|-------------|-----------------------------|
|  Biden      |    Yonglin Wang             |
|  Buttigieg  |    Xiaoyu Lu                |
|  Sanders    |    Yonglin Wang             |
|  Warren     |    Zhuoran Huang            |
|  Yang       |    Xiaoyu Lu                |

Hint: you can double-check the random assignments by running

```
python scripts/assign_annotators.py
```

## Links
- [Sentiment Analysis @ NLP-progress](http://nlpprogress.com/english/sentiment_analysis.html)
