import asyncio
import discord
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
client = discord.Client()

#add the test_project bot token
token = "OTgxNjAwMDQwODk4Mzk2MjMw.GteYmv.fVR3a3gBef1H2J5zmX-lhOduza1DcbJVhMspw0"

#when the bot started, run this part
@client.event
async def on_ready():
    #print your ID and name of bot
    print("Logged in as ")
    print(client.user.name)
    print(client.user.id)

#when the bot received new massage, run this part
@client.event
async def on_message(message):
	#read the page by the ID and receive the level in LostArk homepage
    url = "https://lostark.game.onstove.com/Profile/Character/"+parse.quote(message.content[1:])
    print (url) # print by log
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    #tmpContent = bsObject.find_all(class_='level-info__item')
    tmpContent = bsObject.find_all("div", {"class":"level-info__item"})[0].find_all("span")[1].text

    print(tmpContent)

    #if the bot sent the mesage
    if message.author.bot: 
        #ignore
        return None
    #the ID of the sender of the message is stored in the variable "id"
    #id라는 변수에 메시지를 보낸사람의 ID를 저장하는 부분
    id = message.author.id
    #channel stores the ID of the channel that received the message
    channel = message.channel 
    #if the message start this '!안녕'
    if message.content.startswith('!안녕'): 
        #await client.send_message(channel, '안녕') #the bot said '안녕' in your channel
        await channel.send('안녕')
    else:
        #print the web crawling part by LostArk homepage
        await channel.send("<@"+str(message.author.id)+"> : 레벨\""+message.content[1:]+"\""+str(tmpContent))

client.run(token)