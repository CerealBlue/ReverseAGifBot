from PIL import Image, ImageSequence
import praw
import sys

print ("Authenticating ReverseAGifBot...")

try:
    reddit = praw.Reddit(
                        #This stuff is secret
                        )
except Exception as e:
    print ("ERROR: Coutld not authenticate ReverseAGifBot:\nError Raised:\n\n"+str(e))
    sys.exit()

print ("ReverseAGifBot Authenticated")

subreddit = reddit.subreddit("gifs")

print ("\nActivated for this/these Subreddits:")
print (subreddit.display_name, subreddit.title)

comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body
    if "reverse" in text:
        print (text, comment.author)
