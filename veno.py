import discord
from discord.ext import commands, tasks
from itertools import cycle
import os

client = commands.Bot(command_prefix=["~","-"] ,description="V e n o")
status = cycle(["Higefive des Monats", "CptErde,xSpritneyBeersx,MrPerezTv,fokx1337,Nick0478,Redsnake88,Amplish"])

reaction_list = ['\U0001F1E6', '\U0001F1E7', '\U0001F1E8', '\U0001F1E9', '\U0001F1EA']
lst_emoji = ''
count = 0
vote_list = []

@client.event
async def on_ready():
    change_status.start()
    print("Veno loding...")

@tasks.loop(seconds=3)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def G(ctx):
    await ctx.send(f"**G steht für Gönnen :Venotvtwitch350:")

@client.command()
async def g(ctx):
    await ctx.send(f"**G steht für Gönnen**")

@client.command()
async def Twitch(ctx):
    await ctx.send(f"**https://www.twitch.tv/venomenice**")

@client.command()
async def twitch(ctx):
    await ctx.send(f"**https://www.twitch.tv/venomenice**")

@client.command()
async def Follower(ctx):
    await ctx.send(f"**2,9 Tsd.**")

@client.command()
async def follower(ctx):
    await ctx.send(f"**2,9 Tsd.**")

@client.command()
async def Aufrufe(ctx):
    await ctx.send(f"**490,0 Tsd.**")

@client.command()
async def aufrufe(ctx):
    await ctx.send(f"**490,0 Tsd.**")

@client.command()
async def Top_Clip(ctx):
    await ctx.send(f"**https://www.twitch.tv/venomenice/clip/EmpathicPowerfulWalletDoritosChip?filter=clips&range=all&sort=time**")


@client.command()
async def top_clip(ctx):
    await ctx.send(f"**https://www.twitch.tv/venomenice/clip/EmpathicPowerfulWalletDoritosChip?filter=clips&range=all&sort=time**")


@client.command()
async def Facebook(ctx):
    await ctx.send(f"**https://www.facebook.com/VenoTV**")

@client.command()
async def facebook(ctx):
    await ctx.send(f"**https://www.facebook.com/VenoTV**")

@client.command()
async def Twitter(ctx):
    await ctx.send(f"**https://twitter.com/Venomenice**")

@client.command()
async def twitter(ctx):
    await ctx.send(f"**https://twitter.com/Venomenice**")

@client.command()
async def YouTube(ctx):
    await ctx.send(f"**https://www.youtube.com/user/Venomenice**")

@client.command()
async def youtube(ctx):
    await ctx.send(f"**https://www.youtube.com/user/Venomenice**")

@client.command()
async def version(ctx):
    await ctx.send(f"**0.0.1 Beta**")

@client.command()
async def commands(ctx):
    embed = discord.Embed(title="Hilfe Menü", description="Hier siehst du verschiedene Commands", colour=discord.Color.from_rgb(0, 255, 34), url="https://www.twitch.tv/venomenice")

    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://static-cdn.jtvnw.net/jtv_user_pictures/venomenice-profile_banner-86581132f11e49c2-480.png")
    embed.set_thumbnail(url="https://static-cdn.jtvnw.net/jtv_user_pictures/venomenice-profile_banner-86581132f11e49c2-480.png")

    embed.add_field(name="~G", value="~g")
    embed.add_field(name="~Twitch", value="~twitch")
    embed.add_field(name="~Twitter", value="~twitter")

    embed.add_field(name="~Facebook", value="~facebook")
    embed.add_field(name="~YouTube", value="~youtube")

    embed.add_field(name="~Top_Clip", value="~top_clip")

    embed.add_field(name="~Follower", value="~follower")
    embed.add_field(name="-Aufrufe", value="~aufrurufe")

@client.event
async def on_message(message):

    if message.content.startswith('/vote'):
        msg = message.content[6:]
        msg_list = msg.split()
        global count
        count = len(msg.split())
        count -= 1
        emoji_list = [' ', ':VenoDaumenR:', ':VenoDaumenR:', ':VenoDaumenR:',
                      ':VenoDaumenR:', ':VenoDaumenR:']
        skip_msg = msg_list[0]
        global lst_emoji
        lst_emoji = emoji_list[count]

        if client.user != message.author:
            await message.channel.send(skip_msg)

            for emoji_list, msg_list in zip(emoji_list, msg_list):
                if msg_list == skip_msg:
                    continue
                await message.channel.send(emoji_list + msg_list)

    if message.content.startswith(lst_emoji):
        for i in range(0, count):
            await message.add_reaction(reaction_list[i])


    await ctx.send(embed=embed)
client.run(os.getenv("TOKEN"))
