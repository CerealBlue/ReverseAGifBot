"""Documentation:
python3 upload.py IMAGE_NUMBER TITLE_OF_THE_POST FILE_NAME POST_LINK
"""

# Pull authentication from the auth example (see auth.py)
from auth import authenticate

#Command Line Arguments
import sys

#Simple datetime stuff
from datetime import datetime

def upload_a_gif(client, imageNumber : int, title_of_the_post : str, FileName : str, postLink : str):

	config = {
        'title': str(imageNumber)+"_ReverseAGifBot",
		'name':  str(imageNumber)+"_Reversed",
		'description': "Gif from Reddit post reversed.\nPost:\t"+title_of_the_post+"\nLink:\t {0}".format(postLink)
		}

	print("Uploading image... ")
	image_path = str(FileName)
	image = client.upload_from_path(image_path, config=config, anon=False)
	print("Done")

	return image


# If you want to run this as a standalone script
if __name__ == "__main__":

	client = authenticate()
	image = upload_a_gif(client, sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

print("Image Link: {0}".format(image['link']))
print ("--------------------")
