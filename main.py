"""
TODO: Dodanie wybuchająch kości (Done)
TODO: Dodanie kilku rzutów w jednej komendzie (Done)
TODO: Dodanie modyfikatorów do rzutów (Done - 18.04.2021)
TODO: Modyfikatory do DNDStats (Done - 18.04.2021)
"""

import discord
import random
from discord.ext import commands

scoresDnd = [69, -5, -4, -4, -3, -3, -2, -2, -1, -1, +0, +0, +1, +1, +2, +2, +3, +3, +4, +4, +5]
scoreDndString = ["69", "-5", "-4", "-4", "-3", "-3", "-2", "-2", "-1", "-1", "+0", "+0", "+1", "+1", "+2", "+2", "+3",
                  "+3", "+4", "+4", "+5"]
client = commands.Bot(command_prefix='/')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


async def on_message(message):
    if message.author == client.user:
        return


@client.command()
async def roll(ctx, dice, userModifiers='',aliases=['r' ]):
    embed=discord.Embed(title="Dice Roller", color=0xff0505)
    #Default Variables
    modifierCount = -1
    modifiersArray = []
    #Check if user gave any Modifiers
    if userModifiers == '':
        print("Zero dodatkowych modyfikatorów")
    else:
        modifier = userModifiers
        modifiersArray = modifier.split(',')
        print(modifiersArray)
    #Create a list with needed dice rolls    
    rollsToDo = f'{dice}'
    rollsToDo = rollsToDo.split("+")
    print(rollsToDo)
    #For loop that makes rolls for user
    for roll in rollsToDo:
        #Variable that changes used modifier if needed
        modifierCount += 1  
        #Check if roll is always 1
        if roll == "1d1!":
            embed.add_field(name="1d1!", value="Wynik rzutu to 1 pacanie!", inline=True)
            await ctx.send(embed=embed)
            continue
        #Default Ace State
        ace = False
        toCheck = list(f'{roll}')
        #Check if roll must Ace
        if "!" in toCheck:
            ace = True
            toCheck.remove(toCheck[-1])
            roll = "".join(toCheck)
        split = roll.split("d")
        throwsNumber = int(split[0])
        sidesNumber = int(split[1].strip())
        array = []
        arrayString = []
        #Ace Roll Mechanic
        if ace == True:
            for i in range(int(split[0])):
                array.append(random.randint(1, sidesNumber))
                arrayString.append(str((array[-1])))
                while array[-1] == sidesNumber:
                    array.append(random.randint(1, sidesNumber))
                    arrayString.append("`" + str((array[-1])) + "`")
            print("{}: {}".format(sum(array), arrayString))
            if not modifiersArray:
                embed.add_field(name=f"Wynik rzutu: {throwsNumber}D{sidesNumber}", value=str(sum(array))+" = "+str(arrayString), inline=False)
            else:
                embed.add_field(name="Modyfikator:", value=str(int(modifiersArray[modifierCount])))
                embed.add_field(name=f"Wynik rzutu: {throwsNumber}D{sidesNumber}", value=str(sum(array)+int(modifiersArray[modifierCount]))+" = "+str(array), inline=False)
        #Normal Roll Mechanic
        else:
            for i in range(int(split[0])):
                array.append(random.randint(1, sidesNumber))
            print("{}: {}".format(sum(array), array))
            if not modifiersArray:
                embed.add_field(name=f"Wynik rzutu: {throwsNumber}D{sidesNumber}", value=str(sum(array))+" = "+str(array), inline=False)
            else:
                embed.add_field(name="Modyfikator:", value=str(int(modifiersArray[modifierCount])))
                embed.add_field(name=f"Wynik rzutu: {throwsNumber}D{sidesNumber}", value=str(sum(array)+int(modifiersArray[modifierCount]))+" = "+str(array), inline=False)
        
    await ctx.send(embed=embed)

@client.command(aliases=['dnds', 'dndstats'])
async def dndStats(ctx):
    embed=discord.Embed(title="DND 5E STATISTICS", color=0xff0505)
    for y in range(6):
        array = []
        statsName = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        for x in range(4):
            array.append(random.randint(1, 6))
        array.remove(min(array))
        embed.add_field(name=statsName[y]+":", value=str(sum(array))+" = "+scoreDndString[sum(array)], inline=False)
    await ctx.send(embed=embed)


client.run("ODIwNzExMzYyMTA3MDE1MTc4.YE5JBA.oR1D97MtgvchhsFpnL0TzoJ6KU4")
