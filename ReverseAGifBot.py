from PIL import Image, ImageSequence
from datetime import datetime
from subprocess import run
import pprint
import praw
import sys


def reverseThisGif(link : str):
    print ("\n\tReverseThisGif inititate...")

    im = Image.open(link+".gif")
    frames = [frame.copy() for frame in ImageSequence.Iterator(im)]
    frames.reverse()
    frames[0].save(link+"Reverse.gif", save_all=True, append_images=frames[1:])

    print ("\tReverseThisGif completed Successfully")

def Img(count : int, title : str, FileName : str, link : str):
    run(['python3', 'ImgurHosting/upload.py', str(count), title, FileName+'Reverse.gif', link])

print ("Authenticating ReverseAGifBot...")

try:
    reddit = praw.Reddit(
                        #secret
                        )
except Exception as e:
    print ("ERROR: Coutld not authenticate ReverseAGifBot:\nError Raised:\n\n"+str(e))
    sys.exit()

print ("ReverseAGifBot Authenticated")

subreddit = reddit.subreddit("gifs")

print ("\nActivated for this/these Subreddits:")
print (subreddit.display_name, subreddit.title)
print ("\n\n")

comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body
    if "!reversegif" == text.lower():
        print ("Command Identified:")
        print ("Time:\t"+str(datetime.now()))
        print ("Title:\t"+str(comment.link_title))
        print ("Text:\t"+str(text))
        print ("Author:\t"+str(comment.author))
        print ("-----")
        print ("###Process Begin")

        print ("\tWget Gif inititate")
        run(['wget', '-O', 'test.gif', comment.link_url])
        print ("\tWget gif complete")

        reverseThisGif("test")

        """Start IMGUR Stuff"""

        """run(['mv', 'testReverse.gif', 'ImgurHosting/'])"""

        """print ("\n\tPushing to Imgur")
        Img(0, "test", "test", "NA")
        print ("\tPushing to Imgur Completed")
"""
        print("###Completed")
