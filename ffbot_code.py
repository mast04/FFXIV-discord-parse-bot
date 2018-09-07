#Main coder: u/mast04 @ Yulius Vendetta, Gilgamesh, NA
import discord
import requests
import json
from bs4 import BeautifulSoup as BS
import urllib.request
import random
from Settings import *



def fflogparse (ffdata):
    #to find how many bosses and how many jobs used per boss
    bnum = len(ffdata) #number of bosses

    #to find corresponding boss, job, dps, and percentile
    fflogdictionary = {}
    for x in range(0, bnum):
        if ffdata[x]['encounterName'] in fflogdictionary:
            fflogdictionary[ffdata[x]['encounterName']].update({ffdata[x]['spec'] : [ffdata[x]['total'], ffdata[x]['percentile']]})
        else:
            fflogdictionary[ffdata[x]['encounterName']] = {ffdata[x]['spec'] : [ffdata[x]['total'], ffdata[x]['percentile']]}
    return(fflogdictionary)

def clear_count (ffdata):
    num = len(ffdata) #number of bosses
    bosses = {} #number of jobs per boss
    clears = {} #number of clears per boss
    for x in range(0, num):
        bosses[x] = len(ffdata[x]['specs'])
    for x in range(0, num):
        boss_clear = 0
        for y in range(0, bosses[x]):
            boss_clear = boss_clear + len(ffdata[x]['specs'][y]['data'])
        clears[x] = boss_clear
    return clears


def output(ff_data):
    num = len(ff_data) #number of bosses
    di = {}

    fflist = list(ff_data.keys()) #list of boss names
    for x in range(0, num): #finds number of jobs per boss
        di[x] = len(ff_data[fflist[x]])

    em = discord.Embed(colour=Data_output_color) #start of discord embed output for boss and parses

    for x in range(0, num): #created sentences
        bossname = fflist[x]
        say = ""
        for y in range(0, di[x]):
            percentile = int(ff_data[fflist[x]][list(ff_data[fflist[x]])[y]][1])
            if percentile % 10 == 1 and percentile != 11:
                percent = str(percentile) + "st"
            elif percentile % 10 == 2 and percentile != 12:
                percent = str(percentile) + "nd"
            elif percentile % 10 == 3 and percentile != 13:
                percent = str(percentile) + "rd"
            else:
                percent = str(percentile) + "th"
            deeps = ff_data[fflist[x]][list(ff_data[fflist[x]])[y]][0]
            classjob = list(ff_data[fflist[x]])[y]
            if percentile < 20:
                say = say + classjob + " with " + str(deeps) + " DPS and " + percent + ' percentile. __***SCRUB ALERT!!!***__ \n'
            else:
                say = say + classjob + " with " + str(deeps) + " DPS and " + percent + ' percentile. \n'
        em.add_field(name = bossname, value = say, inline = False) #Addition of fields to the started embed
    return(em)

def bot_talks (name, server, region):
    #API location

    url = "https://www.fflogs.com/v1/rankings/character/" + name + "/" + server + "/" + region + "?api_key=" + fflogkey

    data = requests.get(url) #to obtain the data
    jdata = json.loads(data.text) #transform data to dictionary/list format
    code = data.status_code

    if code == 400:
        return(discord.Embed(title = Not_exist_text, colour=Not_exist_color))
    elif len(jdata) == 0:
        return(discord.Embed(title = Not_available_text, colour=Not_available_color))
    elif len(jdata) == 1:
        return(discord.Embed(title = Hidden_parse_error_text, colour=Hidden_parse_error_color))
    else:
        ff = fflogparse (jdata) #boss, job, dps, percent data

        realname = jdata[0]['characterName']
        charID = str(jdata[0]['characterID'])

        #start of icon image search
        html = urllib.request.urlopen('https://www.fflogs.com/character/id/' + charID)
        soup = BS(html, "html.parser")
        resultsimg = (soup.find("img", {"id" : "character-portrait-image"}))
        imgurl = resultsimg.get('src')

        botsays = output(ff)
        botsays.set_author(name=realname, url = 'https://www.fflogs.com/character/id/' + charID, icon_url=imgurl)

        return(botsays)

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('search'):
        msglist = message.content.split()
        first = msglist[1]

        if len(msglist) > 2:
            second = '_' + msglist[2]
        else:
            second = ""

        ffname = first + second
        html = urllib.request.urlopen("https://www.fflogs.com/search/?term=" + ffname)
        soup = BS(html, "html.parser")

        presence = (soup.find("div", {"class" : "dialog-block"}))
        try:
            len(presence)
        except TypeError:
            await client.send_message(message.channel, embed = discord.Embed(title = Search_not_found_text, colour=Search_not_found_color))
        else:
            try:
                resultsdiv = (soup.find_all("div", {"class" : "result-list"})[1])
            except IndexError:
                resultsdiv = (soup.find("div", {"class" : "result-list"}))
            rawcode = resultsdiv.find_all('a')
            rawinfo = resultsdiv.find_all("div", {"class" : "server"})

            #place in dictionary
            idlink = {}
            n=1
            for rawlink in rawcode:
                idlink[n] = rawlink.get('href')
                n = n + 1
            #place in matching dictionary

            serverinfo = []
            for rawserver in rawinfo:
                serverinfo.append(rawserver.get_text())

            characters = {}
            n=1
            for rawname in rawcode:
                characters[n] = rawname.get_text() + " " + serverinfo[n-1]
                n = n + 1

            #creation of search results
            searchem = discord.Embed(colour=Character_found_color)
            searchbot = ""
            for number, name in characters.items():
                searchbot = searchbot + "%d >> %s \n" % (number, name)
            searchem.add_field(name = "Characters found:", value = searchbot, inline = False)

            if len(searchbot) > 2000:
                await client.send_message(message.channel, embed = discord.Embed(title = Broad_search_error_text, colour=Broad_search_error_color))
            else:
                await client.send_message(message.channel, embed = searchem)

            msg = await client.wait_for_message(timeout=15, author=message.author)
            x = int(msg.content)

            if x in range(1, n):
                searchCH = characters[x].split(' ', 4)
                given = searchCH[0] + ' ' + searchCH[1]
                server = searchCH[4]
                region = searchCH[2]

                botsearch = bot_talks(given, server, region)

                await client.send_message(message.channel, embed = botsearch)
            else:
                await client.send_message(message.channel, embed = discord.Embed(title = Not_a_selection_error_text, colour=Not_a_selection_error_color))

    if message.content.startswith('fflog'):
        msglist = message.content.split()
        first = msglist[1]
        second = msglist[2]

        try: #for multiple server entries
            msglist[3]
        except IndexError:
            msglist = [msglist[0], msglist[1], msglist[2], home_server]

        third = msglist[3]

        name = first + " " + second
        server = third
        region = home_region

        botwords = bot_talks(name, server, region)

        await client.send_message(message.channel, embed=botwords)

    if message.content.startswith('/random'):
        fnum = str(random.randint(1, 999))
        await client.send_message(message.channel, fnum)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(Discord_token)
