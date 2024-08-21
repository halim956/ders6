import os
import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def gdmem(ctx): 
    image_name = random.choice(os.listdir('gdmem'))
    with open(f'gdmem/{image_name}','rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def yardım(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir çevre dostu bilgi verici discord botuyum! içimde bulunan bazı komutlar var $geridönüşümler yazarmısnız.')

@bot.command()
async def geridönüşümler(ctx):
    await ctx.send(f'selam kodlarımda buluna geri dönüşümlere erişmek için $ssd , $kk , $kd , $dahafazlası')

@bot.command()
async def ssd(ctx):
    await ctx.send(f'pet şişelerden sonsuz su döngüsü yapa bilirsin = https://www.youtube.com/watch?v=H4n6m4EaoSw ')

@bot.command()
async def kk(ctx):
    await ctx.send(f'kartondan kasa yapaliriz çünkü paralarınız çalmak için çabalayan bir sürü hırsız var 🕴🕵️‍♂️ = https://www.youtube.com/watch?v=76VUekozHDs  ')

@bot.command()
async def kd(ctx):
    await ctx.send(f'mesela kartondan direksiyon yapıp etsye bağlaya bilir telefondaki arba oynumuza bağlaya biliriz = https://www.youtube.com/watch?v=B941_jDvOY0 ')

@bot.command()
async def dahafazlası(ctx):
    await ctx.send(f'daha fazla kartondan geri dönüşüm için = https://www.youtube.com/watch?v=kyXt5BKxmw0 daha fazla kağıttan geri dönüşüm için = https://www.youtube.com/watch?v=T3XCJZFIYNk  daha fazla alimuyum folyodan geri dönüşüm için = https://www.youtube.com/watch?v=rZp-PKylkwY')

@bot.command()
async def gd(ctx):
    await ctx.send(f'!!dikkat!! lütfen yakınlarınızı uyarın ve sizde uygulayın geri dönüşümleri doğru geri dönüşüm kutularına yollayın kağıtları kağıtlara plastikleri plastiğe camları cama yollayınız çevrenize önem veriniz hiçbir şeyi geri dönüştürmeden bırakmayın iyi günler')






bot.run('gizli token')
