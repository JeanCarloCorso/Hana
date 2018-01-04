# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer 
from chatterbot import ChatBot 

bot = ChatBot('Hana')

conversa = ['Oi', 'Olá', 'Tudo bem com você?', 'Eu estou bem, Obrigado', 'Obrigado', 'Não tem de que :)']
conversa2 = {
    'Qual é o seu nome?', 'Eu me chamo Hana', 
    'É um belo nome!', 'Obrigada',  
    'Quem é você?', 'Eu sou a Hana, uma inteligência artificial criada para tornar as férias do meu criador um pouco mais divertida.',
    'Quem é o seu pai?', 'Meu pai é um jovem cientista da computação chamado Jean Carlo Corso',
    'Quantos anos você tem?', 'Eu nasci em 03/01/2018',
    'Porque você foi criada?', 'Para divertir as pessoas!'
    }

bot.set_trainer(ListTrainer)
bot.train(conversa)
bot.train(conversa2)

while True:
    questao = input("Você: ")
    resposta = bot.get_response(questao)
    if float(resposta.confidence) > 0.5:
        print ('Hana: ', resposta)
    else:
        print ('Eu não sei :(')