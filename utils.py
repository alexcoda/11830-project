"""Preliminary data exploration for 11-830 project. By Alex Coda"""
from collections import Counter

def get_top_users(df, topn):
    """Get the number of posts from topn users."""
    return Counter(df['user_screen_name']).most_common(topn)
    n_posts = sum([v for user, v in top_users])
    return n_posts


def user_mask(df, username):
    """Return a masked df corresponding only to the given username."""
    return df[df['user_screen_name']==username]


def count_top_labels(df, label, topn):
    """Print the percentage that the topn users contribute to a given label."""
    total = sum(df[label])
    top = sum(df.sort_values(by=label, ascending=False)[:topn][label])
    perc = 100. * top / total

    prnt_str = "{0:4} of {1:5} {2:7} tweets are " + \
               "from the top {3:2} users ({4:5.2f}%)"
    print(prnt_str.format(top, total, label, topn, perc))