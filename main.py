import discord
from discord.ext import commands
import asyncio
import random
import string

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# /say command
@bot.tree.command(name="say", description="Make the bot say something")
async def say(interaction: discord.Interaction, message: str):
    # Send ephemeral response first to acknowledge the command
    await interaction.response.send_message("Command executed", ephemeral=True)
    # Send the actual message to the channel
    await interaction.followup.send(message)

# /bsay command with button
class BSayView(discord.ui.View):
    def __init__(self, message: str):
        super().__init__(timeout=300)
        self.message = message

    @discord.ui.button(label='Spam', style=discord.ButtonStyle.danger)
    async def send_five_times(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()

        for i in range(5):
            await interaction.followup.send(self.message)
            await asyncio.sleep(0.5)  # Small delay between messages

        await interaction.edit_original_response(view=self)

@bot.tree.command(name="bsay", description="Create a button that sends a message 5 times when clicked")
async def bsay(interaction: discord.Interaction, message: str):
    view = BSayView(message)
    await interaction.response.send_message(f"Click the button to send: `{message}` 5 times", view=view, ephemeral=True)

# /nitro command
@bot.tree.command(name="nitro", description="Generate a fake Discord Nitro code (for pranks)")
async def nitro(interaction: discord.Interaction):
    # Generate fake nitro code
    fake_code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

    embed = discord.Embed(
        title="🎉 Discord Nitro Gift!",
        description=f"**Congratulations!** You've received a Discord Nitro gift!\n\n**Gift Code:** `{fake_code}`\n\n*Click the link below to claim:*\nhttps://discord.gift/{fake_code}",
        color=0x7289da
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/123456789/987654321/nitro.png")
    embed.set_footer(text="This gift expires in 48 hours!")

    # Send ephemeral response first to acknowledge the command
    await interaction.response.send_message("Command executed", ephemeral=True)
    # Send the embed to the channel
    await interaction.followup.send(embed=embed)

# /console command
@bot.tree.command(name="console", description="Display a fake hacker console (for pranks)")
async def console(interaction: discord.Interaction):
    console_text = """```ansi
[0;32m┌──([0;31mroot💀kali[0;32m)-[[0;37m~[0;32m]
└─[0;31m#[0m [0;32mInitializing Discord API bypass...[0m
[0;33m[INFO][0m Loading exploit modules...
[0;33m[INFO][0m Connecting to Discord servers...
[0;32m[SUCCESS][0m Connected to discord.com:443
[0;33m[INFO][0m Injecting payload...
[0;32m[SUCCESS][0m Payload injected successfully
[0;33m[INFO][0m Escalating privileges...
[0;32m[SUCCESS][0m Administrator access granted
[0;31m[WARNING][0m Firewall detected, bypassing...
[0;32m[SUCCESS][0m Firewall bypassed
[0;33m[INFO][0m Extracting user data...
[0;32m[SUCCESS][0m Data extraction complete
[0;32m[SUCCESS][0m All systems compromised
[0;31m[ROOT][0m Full access granted to Discord API
```"""

    embed = discord.Embed(
        title="🖥️ Hacker Console",
        description=console_text,
        color=0x00ff00
    )

    # Send ephemeral response first to acknowledge the command
    await interaction.response.send_message("Command executed", ephemeral=True)
    # Send the embed to the channel
    await interaction.followup.send(embed=embed)

# /bypass command
@bot.tree.command(name="bypass", description="Show fake Discord API bypass message (for pranks)")
async def bypass(interaction: discord.Interaction):
    bypass_messages = [
        "🔓 **DISCORD API BYPASSED**",
        "✅ Successfully exploited Discord vulnerability CVE-2024-FAKE",
        "🚨 Unauthorized access granted to Discord servers",
        "⚡ Rate limits disabled",
        "🔥 Admin privileges escalated",
        "💀 Full API access achieved"
    ]

    embed = discord.Embed(
        title="🔴 SYSTEM BREACH DETECTED",
        color=0xff0000
    )

    for i, msg in enumerate(bypass_messages):
        embed.add_field(name=f"Step {i+1}", value=msg, inline=False)

    embed.set_footer(text="System compromised")

    # Send ephemeral response first to acknowledge the command
    await interaction.response.send_message("Command executed", ephemeral=True)
    # Send the embed to the channel
    await interaction.followup.send(embed=embed)

# /hack command
@bot.tree.command(name="hack", description="Initiate fake hack sequence (for pranks)")
async def hack(interaction: discord.Interaction):
    hack_messages = [
        "🔥 **SYSTEM INTRUSION DETECTED**",
        "💀 Anonymous has entered the server",
        "⚡ Bypassing server security protocols...",
        "🚨 Firewall breached - Admin access gained",
        "🔓 All channels unlocked",
        "📡 Extracting server data...",
        "💣 Planting backdoor...",
        "🎯 Target acquired - Full control established",
        "👑 Server has been pwned"
    ]

    embed = discord.Embed(
        title="💀 ANONYMOUS ATTACK IN PROGRESS 💀",
        description="```ansi\n[0;31m▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n[0;31m██ [0;37mWE ARE ANONYMOUS[0;31m ██ [0;37mWE ARE LEGION[0;31m ██\n[0;31m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n[0;32mInitiating DDoS attack...\n[0;32mExploiting SQL injection vulnerabilities...\n[0;31mEXPECT US[0m\n```",
        color=0x000000
    )

    for i, msg in enumerate(hack_messages):
        embed.add_field(name=f"⚠️ Alert {i+1}", value=msg, inline=False)

    embed.set_footer(text="Your server belongs to us now")

    # Send ephemeral response first to acknowledge the command
    await interaction.response.send_message("Command executed", ephemeral=True)
    # Send the embed to the channel
    await interaction.followup.send(embed=embed)

# Error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    print(f'Error: {error}')

# Run the bot
if __name__ == "__main__":
    import os
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        print("Please set the DISCORD_BOT_TOKEN environment variable")
        print("You can do this in the Secrets tab in Replit")
    else:
        bot.run(token)
