import random
from palavras_e_dicas import palavraAleatoria, dicaAleatoria
import os
import time
import unidecode

fim_do_jogo = False

lista_jogadores = []

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")
    
    if(erros == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def pegar_quantidade_de_jogadores():
    while True:
        quantidade_jogadores = int(input('Digite a quantidade de jogadores: '))
        if 1 <= quantidade_jogadores <= 10:
            return quantidade_jogadores
        print('Digite uma opção válida.')

def pegar_nome_dos_jogadores(quantidade_jogadores):
    for i in range(quantidade_jogadores):
        nome_do_jogador = input('Digite o nome do jogador: ')
        lista_jogadores.append({'jogador':nome_do_jogador, 'erro': 0})
    return lista_jogadores

def escolher_palavra_e_dica():
    index = int(random.randint(0, 20))
    palavra_secreta = palavraAleatoria(index)
    dica = dicaAleatoria(index) 
    return palavra_secreta, dica

def atribuir_palavra_e_dica_jogador():
    for i in range(len(lista_jogadores)):
        palavra_e_dica = escolher_palavra_e_dica()
        lista_jogadores[i].update(palavra_secreta = palavra_e_dica[0], dica = palavra_e_dica[1])

def pegar_opcao_jogador():
    while True:
        opcao = int(input("Selecione uma opção\n 1- Ler a história do jogo \n 2- "
                        "Escolher a quantidade de jogadores \nDigite 1 ou 2: "))
        if 1 <= opcao <= 2:
            return opcao
        print('Digite uma opção válida')

def selecao_jogo(opcao):
    if opcao == 1:
        print(historia_do_jogo())

    elif opcao == 2:
        quantidades_de_jogadores = pegar_quantidade_de_jogadores()
        nome_jogadores = pegar_nome_dos_jogadores(quantidades_de_jogadores)
        atribuir_palavra_e_dica_jogador()        

def historia_do_jogo():
    print(" _    _   _   _   _     _____   _   _____   ______   _____   ____   _____")
    print("| \  / | | | | | | |   |_   _| | | | ___ | |  __  | |  ___| |  __| |     |")
    print("| _\/_ | | |_| | | |__   | |   | | | ___|  | |__| | |   \_  | |__  |  _  |")
    print("|_|  |_| |_____| |____|  |_|   |_| |_|     |______| |_|\__| |____| |_| |_|")
    print('=' * 150)
    print('SEJAM BEM VINDOS AO JOGO DA FORCA:')
    print('=' * 150)
    print('As origens do JOGO DA FORCA são obscuras, significando não descoberto, mas parece ter surgido na época vitoriana ”, ')
    print('diz Tony Aguarde, autor de The Oxford Guide to Word Games.')
    print('O jogo é mencionado em “Jogos tradicionais” de Alice Bertha Gomme em 1894 sob o nome de “Pássaros,')
    print('feras e peixes”. As regras são simples; um jogador escreve a primeira e a')
    print('última letras de uma palavra e outro jogador adivinha as letras intermediárias. Em outras fontes,')
    print('O jogo é chamado de “Gallows”, “The Game of Hangin” ou “Hanger”.')
    print('=' * 150)
    print('Implementação:')
    print('=' * 150)
    print('Este é um jogo Hangman simples usando a linguagem de programação Python. ')
    print('Iniciantes podem usar isso como um pequeno projeto para aumentar suas habilidades de programação e compreensão da lógica.')
    print('=' * 150)
    opcao_jogador = pegar_opcao_jogador()
    selecao_jogo(opcao_jogador)

def pegar_letra():
    while True:
        chute = input("Digite uma letra: ").upper().strip()
        if chute.isalpha():
            return chute
        print('Você deve digitar uma letra!')

def letras_acertadas():
    for i in range(len(lista_jogadores)):
        palavradavez = lista_jogadores[i]['palavra_secreta']
        letras_acertadas = ["_"]* (len(palavradavez))
        lista_jogadores[i].update(letras_acertadas = letras_acertadas)

def perdeu():
    global fim_do_jogo
    print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
    print(' ░░░░░░░░░░ \033[7;30mVOCÊ PERDEU\033[m ░░░░░░░░░░░')
    print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
    print()
    fim_do_jogo = True

def ganhou():
    global fim_do_jogo
    global vez
    print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
    print(' ░░░░░░░░░░ \033[7;30mVOCÊ GANHOU!\033[m ░░░░░░░░░░░')
    print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
    print()
    fim_do_jogo = True

def rodar_forca():
    global fim_do_jogo
    vez = 0


    while fim_do_jogo == False:
        print(f'Agora é a vez de: {lista_jogadores [vez]["jogador"]}')
        desenha_forca(lista_jogadores[vez]["erro"])
        print(lista_jogadores[vez]['letras_acertadas'])
        print(f"Dica: {lista_jogadores[vez]['dica']}")
        chute = pegar_letra()
        palavradavez = lista_jogadores[vez]['palavra_secreta']
        if chute in unidecode.unidecode(palavradavez.upper()):
            index = 0
            for letra in palavradavez:

                if chute == unidecode.unidecode(letra.upper()):
                    lista_jogadores[vez]['letras_acertadas'][index] = letra

                index = index + 1

            if '_' not in lista_jogadores[vez]['letras_acertadas']:
                print(lista_jogadores[vez]['letras_acertadas'])
                print('você ganhou essa merda!!!')
                ganhou()

        else:
            print(f'você errou, vez do próximo jogador')
            lista_jogadores[vez]['erro'] += 1
            time.sleep(1)
            clear()            
            if lista_jogadores[vez]['erro'] == 7:
                print('você perdeu playboy')
                print(f' A Palavra era {lista_jogadores[vez]["palavra_secreta"]}')

                perdeu()
            else:
                vez += 1
                if vez >= len(lista_jogadores):
                    vez = 0

def jogar():
    opcao_jogador = pegar_opcao_jogador()
    selecao_jogo(opcao_jogador)
    letras_acertadas()
    rodar_forca()
jogar()