# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2) # faz o pc escolher um numero
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Qual a sua jogada? "))
print('\033[1:36mJO!\033[m')
sleep(1)
print("\033[1:36mKEN!\033[m")
sleep(1)
print("\033[1:36mPO!\033[m")
sleep(1)
print('-=' * 15)
print('COMPUTADOR JOGOU {}.'.format(itens[computador]))
print('JOGADOR JOGOU {}.'.format(itens[jogador]))
print('-=' * 15)

if computador ==0:
    if jogador == 0:
        print("\033[4:33mEMPATE\033[m")
    elif jogador == 1:
        print("\033[4:32mJOGADOR VENCEU\033[m")
    elif jogador == 2:
        print("\033[4:31mCOMPUTADOR VENCEU\033[m")
    else:
        print('\033[4:41mJOGADA INVALIDA\033[m')
elif computador == 1:
    if jogador == 0:
        print("\033[4:31mCOMPUTADOR VENCEU\033[m")
    elif jogador == 1:
        print("\033[4:33mEMPATE\033[m")
    elif jogador == 2:
        print("\033[4:32mJOGADOR VENCEU\033[m")
    else:
        print('\033[4:41mJOGADA INVALIDA\033[m')

elif computador == 2:
    if jogador == 0:
        print("\033[4:31mCOMPUTADOR VENCEU\033[m")
    elif jogador == 1:
        print("\033[4:32mJOGADOR VENCEU\033[m")
    elif jogador == 2:
        print("\033[4:33mEMPATE\033[m")
    else:
        print('\033[4:41mJOGADA INVALIDA\033[m')
