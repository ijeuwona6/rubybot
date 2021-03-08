import discord
import random
client = discord.Client()
token = '자신의봇 토큰'

@client.event
async def on_ready():
    print('Client is Ready')
    await client.change_presence(status = discord.Status.online, activity = discord.Game('개임활동'))

@client.event
async def on_message(message):
    if message.content == "관리자출근":
        embed = discord.Embed(colour=0xFF8000, timestamp=message.created_at)
        embed.add_field(name="`관리자 출근안내.`", value="```관리자가 출근하였습니다.```", inline=True)
        embed.set_footer(text=f"{message.author}, 출근완료", icon_url=message.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/807387263179948052/807543596667764756/korea_2.gif")
        await message.channel.send(embed=embed)

    if message.content == "관리자퇴근":
        embed = discord.Embed(colour=0xFF4000, timestamp=message.created_at)
        embed.add_field(name="`관리자 퇴근안내.`", value="```관리자가 퇴근하였습니다.```", inline=True)
        embed.set_footer(text=f"{message.author}, 퇴근완료", icon_url=message.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/807387263179948052/807543596667764756/korea_2.gif")
        await message.channel.send(embed=embed)
       
    if message.content.startswith("코리아도움말"):
        embed=discord.Embed(title="✅KOREA 도움말", description="명령어안내", color=0x00ff56)
        embed.set_author(name="KOREA RP", url="https://discord.gg/Tt7sN6BgGd")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/807387263179948052/807543596667764756/korea_2.gif")
        embed.add_field(name="`!서버온`", value="서버온공지 명령어입니다.", inline=True)
        embed.add_field(name="`!서버오프`", value="서버오프공지 명령어입니다.", inline=True)
        embed.add_field(name="`코리아 인증 @멘션`", value="인증 명령어입니다.", inline=True)
        embed.add_field(name="`코리아 뉴비지원금 @멘션`", value="지원금 완료 명령어입니다.", inline=True)
        embed.set_footer(text="KOREA 도움말이였습니다.")
        embed.set_footer(text=f"{message.author}, ㅣKOREA:RPㅣby 시 호 ♰#0096", icon_url=message.author.avatar_url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/805803410149998652/807881692361523210/unknown.png")
        await message.channel.send(embed=embed) 
        
    if message.content == '!서버온': 
       embed = discord.Embed(title = '🟢 KOREA:RP', description = '```🌐 KOREA 서버 상태 : ON```', color = discord.Color.green())
       embed.add_field(name = "```🎮접속방법```", value = "```🔵 F8 > connect.준비중```", inline=False)
       embed.set_footer(text=f"{message.author}, ㅣKOREA:RPㅣby 시 호 ♰#0096", icon_url=message.author.avatar_url)
       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/807387263179948052/807543596667764756/korea_2.gif")
       await message.channel.send(embed=embed, content = '@everyone') 

    if message.content == '!서버오프': 
       embed = discord.Embed(title = '🔴 KOREA:RP', description = '```🌐 KOREA 서버 상태 : OFF```', color = discord.Color.red())
       embed.add_field(name = "```🌍리붓중```", value = "```🚨 서버접속을 금지합니다.```", inline=False)
       embed.set_footer(text=f"{message.author}, ㅣKOREA:RPㅣby 시 호 ♰#0096", icon_url=message.author.avatar_url)
       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/807387263179948052/807543596667764756/korea_2.gif")
       await message.channel.send(embed=embed, content = '@everyone')   

client.run(token)