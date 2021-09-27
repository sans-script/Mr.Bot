import discord
import os
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?norms':
            await message.channel.send(f'Hello {message.author.name} 👋 {os.linesep}Community Norms: Engaged, Supportive, Inclusive{os.linesep}1- All students are required to agree to the Code of Conduct.{os.linesep}2- Every student is on a level playing field, and we can all learn from one another.{os.linesep}3- Students are not in competition with one another and should be supportive, not competitive.')
        elif message.content == '?help':
            await message.author.send(f"Code of Conduct Violation{os.linesep}To report a Code of Conduct violation, please fill out the form https://docs.google.com/document/u/2/d/1_2Onjpec138LYfuJ2iw58SKtpZsaWlCAUeT3iPkxdrQ/edit. For urgent matters, call our office or email us with the subject line ‘URGENT’ at student@qubitbyqubit.org.")
        elif message.content == 'Hi Mr.Robot':
            await message.channel.send(f'Hi {message.author.name} 👋')

client = MyClient()
client.run('ODkxODI2NjU2NzY1OTYwMTky.YVEATA.GL3KxjNVrS5eUQtf2q3aOv2Po5w')