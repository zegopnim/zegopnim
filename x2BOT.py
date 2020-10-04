import asyncio
import discord
from discord.utils import get

app = discord.Client()


calcResult = 0

@app.event
async def on_ready():
    print("아래 봇으로 로그인 합니다!")
    print(app.user.name)
    print(app.user.id)
    print("================")
    activity = discord.Streaming(name="제곱님", url="https://www.twitch.tv/zegopnim1012")
    await app.change_presence(status=discord.Status.idle, activity=activity)

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.startswith("x2 테스트"):
        id = message.author.id
        await message.channel.send("<@" + str(id) + ">, 테스트완료 오류 없음")
    if message.content.startswith("x2 유튜브"):
        id = message.author.id
        await message.channel.send("<@" + str(id) + ">, https://www.youtube.com/channel/UC0QFI6IaKe7GLZsj32r4-pw")
    if message.content.startswith("x2 트위치"):
        id = message.author.id
        await message.channel.send("<@" + str(id) + ">, https://www.twitch.tv/zegopnim1012")

@app.event
async def on_member_join(member):
    syschannel = member.guild.system_channel.id 
    try:
        embed=discord.Embed(
            title=f'멤버 입장',
            description=f'{member}님이{member.guild}에 입장 했습니다.\n현재 서버 인원수: {str(len(member.guild.members))}명',
            colour=0x00ff00
        )
        embed.set_thumbnail(url=member.avatar_url)
        await client.get_channel(syschannel).send(embed=embed)
    except:
        return None

  
access_token = os.environ["BOT_TOKEN"]
app.run(acces_token)
