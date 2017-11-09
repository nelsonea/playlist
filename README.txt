Erik Nelson

Unix tools project - May 2017

This project runs a python program to scrape tweets that use
the hashtag #NowPlaying or #nowplaying. Using Unix commands, 
two make files extract and sort the collected twitter data 
taking the top 30 songs and ranking them according to the 
number of times they were tweeted (highest to lowest) and 
create either a url that automatically searches the songs 
or an exportable list.    

DIRECTIONS

The command 'make tweets' runs the python program and creates a 
text file called 'tweets.txt' Let make tweets run to collect tweets. 
The longer you run 'make tweets' the more tweets will be scraped. 
'make tweets' can be stopped at any time by pressing 'control + c'.   

Option 1:
A user can enter the command 'make url' which will automatically
generate and open a url that performs a search of the songs, making 
them available to be converted to Spotify.

Option 2:
The command 'make playlist' creates a list of songs from all of the tweets. 
The generated list of songs can then be copy and pasted into the 
textbox here: http://spotlistr.herokuapp.com/#/search/textbox 
followed by clicking 'Search!', choosing a name for the playlist and 
clicking 'Create'. This imports the created playlist into your Spotify 
account if you are logged in.




Python program uses tweepy to get tweets. 

To get tweepy 
git clone https://github.com/tweepy/tweepy.git
python setup.py install 
