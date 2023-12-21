import discord
import os
import random

bot_wins_list = ["I'm the best", "I won", "You're nothing","Is that the best you've got?", "I detonate. You don't."]
jokenpo_list = ["rock", "paper", "scissors"]

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.author == client.user:
            return

        if message.content == "?norms":
            await message.channel.send(f"Hello {message.author.name} 👋 {os.linesep}Community Norms: Engaged, Supportive, Inclusive{os.linesep}1 - All students are required to agree to the Code of Conduct.{os.linesep}2 - Every student is on a level playing field, and we can all learn from one another.{os.linesep}3 - Students are not in competition with one another and should be supportive, not competitive.")

        elif message.content == "rock":
            bot_choice = random.choice(jokenpo_list)
            await message.channel.send(bot_choice)

            if bot_choice == "paper":
                await message.channel.send(random.choice(bot_wins_list))
            elif bot_choice == "scissors":
                await message.channel.send("You won! Nooo")
            else:
                await message.channel.send("It's a tie!")

        elif message.content == "paper":
            bot_choice = random.choice(jokenpo_list)
            await message.channel.send(bot_choice)

            if bot_choice == "scissors":
                await message.channel.send(random.choice(bot_wins_list))
            elif bot_choice == "rock":
                await message.channel.send("Oh no! Paper covers rock.")
            else:
                await message.channel.send("It's a tie!")

        elif message.content == "scissors":
            bot_choice = random.choice(jokenpo_list)
            await message.channel.send(bot_choice)

            if bot_choice == "rock":
                await message.channel.send(random.choice(bot_wins_list))
            elif bot_choice == "paper":
                await message.channel.send("Nooo! Scissors cut paper.")
            else:
                await message.channel.send("Haha it's a tie!")

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTE4NzM3ODc1MDY2MTM0OTQzNg.GJ0n5h.7Xo1y_UvDOChsgXnCm6R-SoksqC-De8ijYek0o')
