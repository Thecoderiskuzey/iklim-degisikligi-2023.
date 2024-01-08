import discord
from discord.ext import commands
import random
import requests
from ai_fn import aiws
import random
p = ["🤣","😀","😁","😂","🤣","😃","😄","😎","😋","😊","😉","😆","😅","😍","😘","🥰","😗","😙","🥲","🤔","🤩","🤗","🙂","☺️","😚","🫡","🤨","😐","😑","😶","🫥"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='/', intents=intents)
@bot.command()
async def emoji(ctx):
    x = random.choice(p)
    await ctx.send(random.choice(p))
@bot.command()
async def aktif(ctx):
    await ctx.send("Bu makine aktivdir!👋")
@bot.command()
async def bilgi(ctx):
    await ctx.send("Bilgi: Yapımcısı Osman Kuzey Haytan"+"\n"+"Nesili tükenmekte olan canlılar bizim için çok önemli olabilir. Şu örneğe bakın" + "\n" + "a|>b|>c|>d|>e|fotosentez|"+ "\n" + "bu örnekte yırtıcı|>av (|fotosentez| Fotosentez yapıldığını gösterir " + "\n" + "a b ve e yer,b sadece c yer , c sadece dyi yer ve e ile d fotosentez yapar"+ "\n" + "bu örnekte d canlısının nesli tükenirse sırasıyla c,b ve a nin nesli tükenir ve enin sayısı artar(bu bizim için kötü birşey olabilir) ")
@bot.command()
async def ayirt(ctx, link):
    response = requests.get(link)
    file = open("sample_image.png", "wb")
    file.write(response.content)
    file.close()

    
    sonuc = aiws()
    
    await ctx.send(sonuc)
    


def get_duck_image_url():    
    url = "https://random-d.uk/api/random"
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)



























































bot.run("no cod for u")
