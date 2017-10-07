# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 01:45:56 2017

@author: SG/guardian-of-code
"""
intro = """
        \n\n Welcome one and all to SG's amazing game of tic tac toe!!!
         INSTRUCTIONS:
              To place an 'X' or 'O' simply enter the co-ordinate of the cell
              for example: to place a 'O' in top left corner type a0

         RULES (as if we need them):
             1. This game is for 2 players.
             2. They alternatnatively place an X or O in the cell the wish.
             3. First to get three of X's or O's in a row or coloum or diagonal
                wins.
             4. Enjoy...
       """

n = ['a0', 'a1', 'a2', 'b0', 'b1', 'b2', 'c0', 'c1', 'c2']
d = {w: ' ' for w in n}
print(intro)


def new_game():
    print(intro)
    global d
    global n
    n = ['a0', 'a1', 'a2', 'b0', 'b1', 'b2', 'c0', 'c1', 'c2']
    d = {w: ' ' for w in n}


def board_1():
    print('   0   1   2')
    print('a ', d['a0'], '|', d['a1'], '|', d['a2'])
    print('  ---+---+---')
    print('b ', d['b0'], '|', d['b1'], '|', d['b2'])
    print('  ---+---+---')
    print('c ', d['c0'], '|', d['c1'], '|', d['c2'])

board_1()
i = 0


def play_another():
    print('\nPlay anothe Game ?[yes/no]\n')
    z = input()
    if z == 'yes':
        global i
        i = 0
        new_game()
    else:
        raise SystemExit


def check_if_empty(i):
    x = input()
    if d[x] == 'X' or d[x] == 'O':
        print('this spot is alreday picked!Choose another location..\n')
        check_if_empty(i)
    elif i % 2 == 0:
        player1(x)
    else:
        player2(x)


def winner_check(x):
    global l
    l = [
        [j for j in n[0:3]], [j for j in n[3:6]], [j for j in n[6:]],
        [j for j in n[0:7:3]], [j for j in n[1::3]], [j for j in n[2::3]],
        [j for j in n[0::4]], [j for j in n[2:7:2]]
        ]
    k = 0
    c = 0
    while k < 8:
        c = 0
        p = False
        for w in l[k]:
            if d[w] == d[x]:
                c += 1
            else:
                p = False
            if c == 3:
                p = True
                break
        k += 1
        if c == 3:
            break
    return (p)


def player1(O):
    d[O] = 'O'
    if(winner_check(O)):
        print('\nPlayer1 has won\nHooray!!! \nPlayer2 better luck next time\n')
        board_1()
        play_another()
    board_1()


def player2(X):
    d[X] = 'X'
    if(winner_check(X)):
        print('\nPlayer2 has won\nHooray!!! \nPlayer1 better luck next time\n')
        board_1()
        play_another()
    board_1()
i = 1
while i < 11:
    if i == 10:
        print('\nGame is a draw\n')
        i = 0
        play_another()
    elif(i % 2 == 0):
        print('\nplayer1\'s turn')
        print('enter the location of \'O\' to be place:')
        check_if_empty(i)
    else:
        print('\nplayer2\'s turn')
        print('enter the location of \'X\' to be place:')
        check_if_empty(i)
    i += 1
