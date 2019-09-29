import praw
import re
import random

bot_quotes = \
[
" xxx",
" yyy",
"zzz ",
]

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("<desired subreddit>")

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("<keyword to trigger bot>", comment.body, re.IGNORECASE):
            bot_reply = "Bot says: " + random.choice(bot_quotes)
            comment.reply(bot_reply)
            print(bot_reply)
