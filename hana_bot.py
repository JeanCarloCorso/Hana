# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer 
from chatterbot import ChatBot 

bot = ChatBot('Hana')

conversa = ['Oi', 'Olá', 'Tudo bem com você?', 'Eu estou bem, Obrigado']
arquivo = open("exemplo.txt", 'r')

bot.set_trainer(ListTrainer)
bot.train(conversa)
bot.train(arquivo)

while True:
    questao = input("Você: ")
    resposta = bot.get_response(questao)
    if float(resposta.confidence) > 0.5:
        print ('Hana: ', resposta)
    else:
        print ('Eu não sei :(')