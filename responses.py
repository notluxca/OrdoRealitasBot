import data
import json
import numpy
import random
import discord


appIconUrl = "https://media.discordapp.net/attachments/919135220245082124/1131228682657214484/Screenshot_20230617_230829_Instagram.jpg?width=341&height=341"

# armazenando os dados de cada personagem
charsData = data.data

# aqui ficar responsavel por rolar os dados
# descobrir quem é o persongem da pessoa que enviou a mensagem e enviar os dados baseados nela
# baseado no owner da mensagem retorna o index dele no charsData
def makeSearch(owner):
    for index in range(0,charsData.__len__()):
        if owner == charsData[index].get("owner"):
            return index



def handle_response(message):
    index = makeSearch(str(message.author))
    pfp = message.author.avatar
    charName = charsData[index].get("character")
    # print user who sent the message
    print(f"{message.author}: {message.content}")
    c_message = message.content.lower() 
    match c_message:
        case "tdv" | "teste de vigor":
            return tdv(message)
        case "tda" | "teste de agilidade":    
            return tda(message)
        case "tdf" | "teste de força":    
            return tdf(message)
        case "tdi" | "teste de inteligência":    
            return tdi(message)
        case "tdp" | "teste de presença":    
            return tdp(message)
        
        case "-mychar":
            return whoAmI(message)
        
        case "-ajuda":
            return "Esse bot foi desenvolvido por Lucas Fernandes\nPara mais informações acesse: "
    
    

    
    if c_message.split(" ")[0] == "rolar":
            rollRequest = c_message.split(" ")
            rolled = rollRequest[1]
            rollRequest = rollRequest[1].split("d")
            
            if int(rollRequest[0]) != 1:
                results = []
                for i in range(0,int(rollRequest[0])):
                    results.append(random.randint(1,int(rollRequest[1])))
                count = 0
                for i in results:
                    count += i
                if rollRequest[1] == 20:    
                    if lookForCritic(results):
                        return criticRollEmbed(message, results, rolled, count) 
                else: 
                    print(rollRequest)
                    return rollEmbed(message, results, rolled, count)
            

            else:
                result = random.randint(1,int(rollRequest[1]))
                return rollEmbed(message, result)
    else:
        return ""

    # create embed
    # return embed

# teste de vigor FUNCIONANDO
def tdv(message):
    results = []
    index = makeSearch(str(message.author))
    pfp = message.author.avatar
    charName = charsData[index].get("character")
    for i in range(0, int(charsData[index].get("_vigor"))):
        results.append(random.randint(1,20))

    return testEmbed(
        charName, "Vigor", results, charsData[index].get("charPcUrl")
    )
    

def tda(message):
    results = []
    index = makeSearch(str(message.author))
    pfp = message.author.avatar
    charName = charsData[index].get("character")
    for i in range(0, int(charsData[index].get("_agilidade"))):
        results.append(random.randint(1,20))

    return testEmbed(
        charName, "Agilidade", results, charsData[index].get("charPcUrl")
    )


def tdi(message):
    results = []
    index = makeSearch(str(message.author))
    pfp = message.author.avatar
    charName = charsData[index].get("character")
    for i in range(0, int(charsData[index].get("_intelecto"))):
        results.append(random.randint(1,20))
    
    return testEmbed(
        charName, "Inteligência", results, charsData[index].get("charPcUrl")
    )


def tdp(message):
    results = []
    index = makeSearch(str(message.author))
    pfp = message.author.avatar
    charName = charsData[index].get("character")
    for i in range(0, int(charsData[index].get("_presença"))):
        results.append(random.randint(1,20))
    
    return testEmbed(
        charName, "Presença", results, charsData[index].get("charPcUrl")
    )

def tdf(message):
    results = []
    index = makeSearch(str(message.author))
    pfp = message.author.avatar
    charName = charsData[index].get("character")
    charPic = charsData[index].get("charPcUrl")
    for i in range(0, int(charsData[index].get("_força"))):
        results.append(random.randint(1,20))    
    # cria o embed
    return testEmbed(
        charName, "Força", results, charsData[index].get("charPcUrl")
    )


# ------------ EMBEDS AREA --------------

def testEmbed(charName, testType, results, picUrl):
    embed = discord.Embed(   title = f"Resultado: {max(results)}",
                             description= f"dados: {results}",
                             colour=0x00f080)
    embed.set_author(name=f"{charName} fez um Teste de {testType}", icon_url=picUrl)
    return embed
    

def whoAmI(message):
    index = makeSearch(str(message.author))
    charName = charsData[index].get("character")
    charPic = charsData[index].get("charPcUrl")
    userPic = message.author.avatar
    embed = discord.Embed()

    embed.set_author(name=f"Você está jogando com {charName}",
                 icon_url=userPic)

    embed.set_image(url=charPic)
    # get active person char
    return embed
    ...

# embed para dados em geral
def rollEmbed(message, results, whatRolled, resultsSum):
    embed = discord.Embed(title=f"Resultado: {max(results)}",
                      description=f"soma total: {resultsSum}")

    embed.set_author(name=f"{message.author} rolou {whatRolled}", icon_url=message.author.avatar)

    embed.set_thumbnail(url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4bcc2548-937b-4948-a8de-df85c179759b/dclcb4s-c9b126cf-505d-4d7b-a25f-9b0df66b5d92.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzRiY2MyNTQ4LTkzN2ItNDk0OC1hOGRlLWRmODVjMTc5NzU5YlwvZGNsY2I0cy1jOWIxMjZjZi01MDVkLTRkN2ItYTI1Zi05YjBkZjY2YjVkOTIuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0._JHgAH_NO6rGuqKPEApTvIy8pgFcVOdCG41ByHyaRI4")

    embed.set_footer(text=f"dados: {results}")

    return embed

def criticRollEmbed(message, results, whatRolled, resultsSum):
    embed = discord.Embed(title=f"Resultado: {max(results)}",
                      description=f"ACERTO CRITICO!\nsoma total: {resultsSum}", colour=0x1eff00)

    embed.set_author(name=f"{message.author} rolou {whatRolled}", icon_url=message.author.avatar)

    embed.set_thumbnail(url="https://media4.giphy.com/media/3oriNPdeu2W1aelciY/giphy.gif?cid=ecf05e477kkd0jk7u2594mvgxk3pzvgl8fh8svtt6vtdck70&ep=v1_gifs_search&rid=giphy.gif&ct=g")

    embed.set_footer(text=f"dados: {results}")

    return embed
    

def lookForCritic(array):
    for i in array:
        if i == 20:
            print("CRITIC FOUND")
            return True
            
    return False