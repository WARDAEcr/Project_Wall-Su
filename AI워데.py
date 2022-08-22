import discord
from discord.ext import commands

game = discord.Game("폭8중")
bot = commands.Bot(command_prefix='!', status=discord.Status.online, activity = game)
client = discord.Client()
print(len(client.guilds))
@bot.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.endswith("월"):
        file = discord.File("picture\월수.jpg")
        await message.channel.send(file=file)
        await message.channel.send("월수")
    if message.content.endswith("와"):
        file = discord.File("picture\와플근육.jpg")
        await message.channel.send(file=file)
        await message.channel.send("와플근육")
    if message.content.endswith("궁"):
        file = discord.File("picture\궁예 근육.jpg")
        await message.channel.send(file=file)
        await message.channel.send("..누가 에1엑따 소리를 내었는가?")
    if message.content.endswith("말"):
        file = discord.File("picture\말벌아저씨.jpg")
        await message.channel.send(file=file)
        await message.channel.send("말벌 잡1았다")
    if message.content.endswith("민"):
        file = discord.File("picture\민초 근육.jpg")
        await message.channel.send(file=file)
        await message.channel.send("민트초코는 사1랑입니다 여러분!")
    if message.content.endswith("미"):
        file = discord.File("picture\미란이.jpg")
        await message.channel.send(file=file)
        await message.channel.send("내 이름은 미라니~!")
    if message.content.endswith("빨"):
        file = discord.File("picture\빨리빨리 근육.jpg")
        await message.channel.send(file=file)
        await message.channel.send("빨리빨리 근육")
    if message.content.endswith("좀"):
        file = discord.File("picture\좀비왕 조.jpg")
        await message.channel.send(file=file)
        await message.channel.send("좀비왕 조")
    if message.content.endswith("야"):
        file = discord.File("picture\야 너두 근육.jpg")
        await message.channel.send(file=file)
        await message.channel.send("야,너두 에1엑따 할수 있어")
    if message.content.endswith("아"):
        file = discord.File("picture\아뚜임렛.jpg")
        await message.channel.send(file=file)
        await message.channel.send("나는 수박을 사랑하는 사나이다")
    if message.content.endswith("명"):
        file = discord.File("picture\명탐정 근난.jpg")
        await message.channel.send(file=file)
        await message.channel.send("내 이름은 근난,탐1정이죠")
    if message.content.endswith("송"):
        file = discord.File("picture\송아지 근육.png")
        await message.channel.send(file=file)
        await message.channel.send("어린 송아지가 부두막에 앉아 울1고 있어요!")
    if message.content.endswith("코"):
        file = discord.File("picture\코끼리 근육.jpg")
        await message.channel.send(file=file)
        await message.channel.send("뿌오오오오1ㅗ오오오ㅗ오")
    if message.content.endswith("허"):
        file = discord.File("picture\허기워기 근육.jpg")
        await message.channel.send(file=file)
        await message.channel.send("허기워기 근육")
    if message.content.endswith("장"):
        file = discord.File("picture\장개방.jpg")
        await message.channel.send(file=file)
        await message.channel.send("빵빵 터뜨려주1지")
    if message.content.endswith("븅신"):
        file = discord.File("picture\김븅ㅅ.jpg")
        await message.channel.send(file=file)
        await message.channel.send("븅신")
    if message.content.endswith("빈"):
        file = discord.File("picture\빈약한.jpg")
        await message.channel.send(file=file)
        await message.channel.send("빈약한")
    if message.content.endswith("강"):
        file = discord.File("picture\강력한.jpg")
        await message.channel.send(file=file)
        await message.channel.send("강력한")
    if message.content.endswith("똥"):
        file = discord.File("picture\똥막대기 근육.jpg")
        await message.channel.send(file=file)
        await message.channel.send("똥을 1972년 동안 싸1지 못했다 이런 얘기에요")
    if message.content.endswith("재"):
        file = discord.File("picture\재배맨.jpg")
        await message.channel.send(file=file)
        await message.channel.send("재배맨!")
    if message.content.endswith("주"):
        file = discord.File("picture\주빡빡.jpg")
        await message.channel.send(file=file)
        await message.channel.send("이런 미친,난 여기서 빠1져나가야겠어")
    if message.content.endswith("오"):
        file = discord.File("picture\오징어 근육.jpg")
        await message.channel.send(file=file)
        await message.channel.send("내 이름은 오오오징어 근육")
    if message.content.endswith("촉"):
        file = discord.File("picture\촉촉이.jpg")
        await message.channel.send(file=file)
        await message.channel.send("나의 이룸은 촉크촉이")
    if message.content.endswith("나"):
        file = discord.File("picture\나여캐.jpg")
        await message.channel.send(file=file)
        await message.channel.send("존1나 멋있어요")
    if message.content.endswith("ㅠ"):
        file = discord.File("picture\눈물의 요정.jpg")
        await message.channel.send(file=file)
        await message.channel.send("말도 안된다고호홓호호홓호")
    if message.content.endswith("김"):
        file = discord.File("picture\김근육.jpg")
        await message.channel.send(file=file)
        await message.channel.send("병1신을 만들어주겠다")
        bot.run('MTAwNzc2NTg5NDk5MjI1MzA5OQ.GK11JG.dB7WFpFlRXOKPMRAaXMHsAmK6XcrNP7vdysUSM') #<- insert your bot token!