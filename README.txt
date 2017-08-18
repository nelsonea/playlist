Erik Nelson

Unix tools final project - May 10, 2017

This project runs a python program to get all tweets as they are 
tweeted with the hashtag #NowPlaying or #nowplaying and creates a 
playlist with the top 30 most tweeted songs. 

Option 1:
A user can copy and paste the link created by 'make url' into their
browser and then choose what format they want to convert to.    

Option 2:
The generated list of songs can then be copy and pasted into the textbox here
http://spotlistr.herokuapp.com/#/search/textbox followed by clicking
'Search!' then making a name for the playlist and clicking 'Create'. 
This imports the playlist created into your Spotify account if you are 
logged in.


The command 'make tweets' runs the python program and creates a text file called 'tweets.txt' 

The command 'make playlist' creates a list of songs from all of the tweets 

The command 'make url' creates the url that can be copy and pasted into the browser



Python program uses tweepy to get tweets, to get tweepy ...
git clone https://github.com/tweepy/tweepy.git
python setup.py install 
