import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("<desired subreddit>")

#getting the top 5 posts in subreddit
for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
