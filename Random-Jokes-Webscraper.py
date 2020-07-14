import random
import praw
#random joke generator
from tkinter import *

root = Tk()

def random_joke():
    reddit = praw.Reddit(client_id = 'B69mb6gi7dkJrg',client_secret = 'ln-itHfMFQblfCCTFmguh9Ok3b0', user_agent = 'Kyle' )
    jokes_list = []
    jokes = reddit.subreddit('Oneliners').hot(limit=100)
    for post in jokes:
        jokes_list.append(post.title)
    
    answer = random.choice(jokes_list)
    label = Label(text = answer)
    label.pack()

myButton = Button(text = 'Random Joke', command = random_joke)
myButton.pack()


root.mainloop()

