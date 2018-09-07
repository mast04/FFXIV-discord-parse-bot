# FFXIV-discord-parse-bot

Description: A python3 based Discord bot that pulls FFXIV raid data from FFLog.

Purpose: To allow the user to personally own the Discord bot without having to rely on 3rd party services

Quick commands:
1) `fflog [first name] [last name] [server*]` - Quickly pulls up a specific individual. The server field is optional if you searching in default server
2) `search [search field]` - To search the player through multiple server/regions
3) `/random` - random number generatior from 1-999

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
Setting up python3: 
1. Go to [python.org](http://python.org) and download the later release of Python 3.
1. Install the following packages: [discord], [bs4], and [random]. As for [urllib.request], [json], and [requests], I believe they should come with the Python 3, but you are welcome to try to install them just to make sure you have them. 
    1. On Windows, in order to install the modules, open Powershell, which can be found with "Windows logo key + S", and use the following code `py -3 -m pip install discord` by replacind `discord` with the desired module names.
    
Obtaining a FFLog key:
1. Register or log in on https://www.fflogs.com/
1. Click on your icon of the top right. This should bring a right sided menu, where you are going to need to click on the "Gear" image, which represents settings.
1. At the bottom of the page, you should see a "Web API Keys" tab with "Generate Keys" button in the middle. Click on "Generate Keys".
1. Now you should be seeing two keys: a public one and a private one. We want to obtain the public key.
1. Copy and paste the Public key in the **fflogkey** filed in the **Settings.py** file (open it with a wordpad)
    1. Make sure that the Token value is within the quotations, when placed in the **Settings.py**
    1. Save the file

    
Creating and obtaining discord bot key:
1. A bot can be created with Discord at https://discordapp.com/developers. Log in and click on "Create and application" to get started
1. Give it your preferred name then switch to the "Bot" tab in the "Settings" menu on the left side of the page.
1. Click on "Add Bot" and, when prompted,  do comfirm your intentions.
1. Now, on this page, copy the "Token". This Discord Token will be needed to connect to the Discord Bot you just created.
1. Copy and paste the Token in the **Discord_token** filed in the **Settings.py** file (open it with a wordpad)
    1. Make sure that the Token value is within the quotations, when placed in the **Settings.py**
    1. Save the file
    
Adding the Discord bot to the chat room:
1. In the https://discordapp.com/developers page, select your bot and make sure you are in the "General Information" tab of the "Settings" menu.
1. From here we want to obtain the listed "CLIENT ID".
1. The "CLIENT ID" will be inserted in the following link: `https://discordapp.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot&permissions=0` with `YOUR_CLIENT_ID` replaced with the actual code.
1. By going to the link, while logged in discord, will allow you add the bot to any chat room for which you are allow to do such action.

For a picture guide on how to obtain a Discord token and add a bot, here is a link; however, the information is a bit outdate as at the writing of this text: https://discordpy.readthedocs.io/en/rewrite/discord.html

Finalizing and starting the Bot code:
1. By opening the **Settings.py** file (open it with a wordpad), we are able to access a bunch of setting for the bot.
1. The top two settings should be tokens that you obtain from discord and fflogs. These should not be altered in the future.
1. The following two field should be related to the prefered server/region. These fields should be changed to your server/region in order to allow focused searched with the `fflog [first name] [last name]` command.
1. The #error color fields describe the color of the left edge of the discord bot output for whenever the parse data is not present.
    1. The color number is the RBG Hex number and they can be obtained by quick google search or from websites such as https://www.rapidtables.com/web/color/RGB_Color.html
    1. Place the number directly after `0x` such as in `0x832133` for `832133` which represents a maroon red.
1. The #error text output fields are the text messages for whenever the parse data is not present. 
    1. These should stay in quotations for correct output.
1. The #correct output color fields describe the color of the left edge of the discord bot output for whenever there is data.
    1. Change color as described above.
1. The #the burn field is a message to shame bad percentiles.
    1. This should also stay in quotations for correct output.
1. Save the changes!
    
If you followed the whole guide up to this point, thanks for reading. Just start the code by running **ffbot_code.py** and enjoy. For windows, double clicking the code should open and start the python code.
