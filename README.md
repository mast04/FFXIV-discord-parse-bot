# FFXIV-discord-parse-bot

Description: A python3 based Discord bot that pulls FFXIV raid data from FFLog.

Purpose: The purpose of this piece of code, is to allow the used to personally own the Discord bot 
without having to rely on 3rd party services

Quick commands:
1) fflog [first name] [last name] [server*] - Quickly pulls up a specific individual. The server field is optional if you searching in default server
2) search [first name] [last name]

### Notes
This discord bot is one of my first coding works and, even though there dont seem to be any major bugs, 
you might find some redundant coding; however, they should not be affecting the performance of the bot.

The code uses a few python modules that you might have/need to install. 1)Discord 2)urllib.request and bs4 
3)json and requests 4)random, which I will try to explain how to install for the people new to python

1) Discord is used to connect with the discord service. All the credit to those great souls that brought us such a great tool.
2) urllib.request and bs4 were used to obtain the http code of fflog's search results to allow for cross server/region searchs.
It is to my understanding that usually website developers dislike the usage such codes(??). Sorry if that is case.
3) json and requests were used to obtain the JSON data from the FFlog API. I believe that requests and urllib.request might be interchangeble;
however, the code works as of now and I don't feel the need to change that. (Also redundancy due to my beginner skills)
4) Random was placed as a fun feature to allow the use of "/random" through the discord bot.

As for running the code, I personally suggest the use of a Raspberry Pi running a Linux distribution for hosting the bot; 
however, Amazon AWS is also a nice and free (for the first 12 months) option but, from experience, I found AWS harder to work with.
Of course, you can always start the code at your main computer whenever you need the bot to be alive.

### How to:
1 - 
