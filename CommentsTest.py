__author__ = 'Radostin'
import praw
import operator

r = praw.Reddit(user_agent='TestRComments1.1')

subreddit = r.get_subreddit('programming')

submissions = subreddit.get_hot(limit=3)

html = "<html><table border='1'>"

for submission in submissions:
    html += "<tr><td colspan='3'><b>" + str(submission) + "</b></td></tr>"
    submission.replace_more_comments(limit=None, threshold=0)
    flat_comments = praw.helpers.flatten_tree(submission.comments)
    sorted_comments = sorted(flat_comments, key=operator.attrgetter("score"), reverse=True)
    sorted_comments = sorted_comments[0:3]
    for comment in sorted_comments:
        html += "<tr><td>" + str(comment.score) + "</td><td colspan='2'>" + comment.body + "</td></tr>"

html += "</table></html>"

outfile = open("test.html", "w+")
outfile.write(html.encode('utf-8'))
outfile.close()
