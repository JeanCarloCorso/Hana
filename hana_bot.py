from chatterbot.trainers import ListTrainer 
from chatterbot import ChatBot 

bot = ChatBot('Hana')

conversa = ['Oi', 'Ola', 'Tudo bem com voce?', 'Eu estou bem, Obrigado']

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    quest = input("Voce: ")
    resposta = bot.get_response(quest)
    print ("Hana: ", resposta)
