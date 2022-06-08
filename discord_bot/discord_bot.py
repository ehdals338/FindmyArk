import asyncio
import discord
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
client = discord.Client()

#add the test_project bot token
#must change this token!!!!!
token = "OTg0MTI1NTQyNDgxNjcwMjA0.GdE6KY.sW9_N4ys2g1zLPhfDVeaxDPqN4tSkGRIs3C_D0"

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
    #tmpContent = bsObject.find_all(class_='level-info__item') 원정대, 전투 레벨
    tmpContent = bsObject.find_all("div", {"class":"level-info__item"})[0].find_all("span")[1].text
    #tmpContent = bsObject.find_all(class_='level-info2__item') 아이템 레벨
    item_tmpContent = bsObject.find_all("div", {"class":"level-info2__item"})[0].find_all("span")[1].text

    if tmpContent:
        print(tmpContent)
        print(item_tmpContent)
    else:
        print("Not Found")

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
        await channel.send("<@"+str(message.author.id)+"> : \""+message.content[1:]+"\" ")
        await channel.send("전투: "+str(tmpContent)+" 아이템: "+str(item_tmpContent))

client.run(token)