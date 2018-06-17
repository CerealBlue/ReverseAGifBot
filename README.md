# ReverseAGifBot
`v 0.1.1`

A bot made for Reddit to reverse gif's submitted only to the subreddit `/r/gifs`. The trigger command is:<br/>
&nbsp;`!reversegif`<br/><br/>

Imgur API Call documentation:<br>
&nbsp;`python3 upload.py Image_Number Title_of_the_Post File_Name Link_of_the_Post`<br/><br/>
&nbsp;`Image_Number` - int - The total number of gifs processed till datetime<br/>
&nbsp;`Title_of_the_Post` - str - The name of the post<br/>
&nbsp;`File_Name` - str - The file which the gif is saved as (that is ultimately uploaded)<br/>
&nbsp;`Link_of_the_Post` - str - The link of the post on Reddit that this gif was asked to be reversed
