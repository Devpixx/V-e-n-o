import discord
from discord.ext import commands, tasks
from itertools import cycle
import os

client = commands.Bot(command_prefix="~")
status = cycle(["Higefive des Monats", "Savas"])

@client.event
async def on_ready():
    change_status.start()
    print("Veno loding...")

@tasks.loop(seconds=3)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def G(ctx):
    await ctx.send(f"**G steht für Gönnen**")

@client.command()
async def Twitch(ctx):
    await ctx.send(f"**https://www.twitch.tv/venomenice**")

@client.command()
async def Follower(ctx):
    await ctx.send(f"**2,9 Tsd.**")

@client.command()
async def Aufrufe(ctx):
    await ctx.send(f"**490,0 Tsd.**")

@client.command()
async def Top_Clip(ctx):
    await ctx.send(f"**https://www.twitch.tv/venomenice/clip/EmpathicPowerfulWalletDoritosChip?filter=clips&range=all&sort=time**")

@client.command()
async def Facebook(ctx):
    await ctx.send(f"**https://www.facebook.com/VenoTV**")

@client.command()
async def Twitter(ctx):
    await ctx.send(f"**https://twitter.com/Venomenice**")


@client.command()
async def YouTube(ctx):
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

    embed.add_field(name="~G", value="value1")
    embed.add_field(name="~Twitch", value="value1")
    embed.add_field(name="~Twitter", value="value1")

    embed.add_field(name="~Facebook", value="value1")
    embed.add_field(name="~YouTube", value="value1")

    embed.add_field(name="~Clear", value="value1")
    embed.add_field(name="~Top_Clip", value="value1")

    embed.add_field(name="~Follower", value="value1")
    embed.add_field(name="Aufrufe", value="value1")


    await ctx.send(embed=embed)

client.run(os.getenv("TOKEN"))