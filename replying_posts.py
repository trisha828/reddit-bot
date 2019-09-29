import praw
import pdb
import re
import os


# Creating Reddit instance
reddit = praw.Reddit('bot1')

# Adding to empty list IF not run before
if not os.path.isfile("replied_posts.txt"):
    replied_posts = []

# else load list of replied posts
else:
    # open & read as list + remove  empty values
    with open("replied_posts.txt", "r") as f:
        replied_posts = f.read()
        replied_posts = replied_posts.split("\n")
        replied_posts = list(filter(None, replied_posts))

# Get the top 5 values from the subreddit
subreddit = reddit.subreddit('<subreddit name>')
for submission in subreddit.hot(limit=10):
    #print(submission.title)

    # If we haven't replied to this post before
    if submission.id not in replied_posts:

        # Do a case insensitive search
        if re.search("<user keyword>", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("<bot auto reply")
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            replied_posts.append(submission.id)

# Write our updated list back to the file
with open("replied_posts.txt", "w") as f:
    for post_id in replied_posts:
        f.write(post_id + "\n")
