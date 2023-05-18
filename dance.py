# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:18:35 2023

@author: Andrew 
"""
from random import randint
import pgzrun
import pygame
import pgzero
import random
from pgzero.builtins import Actor
from random import randint
import os

music_dir = 'music'
music_files = [f for f in os.listdir(music_dir) if f.endswith('.ogg')]
selected_music = random.choice(music_files)

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

move_list = []
display_list = []

score = 0
current_move = 0
count = 4
dance_length = 4

say_dance = False
show_countdown = True
moves_complete = False
game_over = False

dancer = Actor("dancer-start")
dancer.pos = CENTER_X - 70, CENTER_Y - 40

up = Actor("up")
up.pos = CENTER_X - 200, CENTER_Y + 110  # Shifted 200 pixels to the left

right = Actor("right")
right.pos = CENTER_X - 140, CENTER_Y + 170  # Shifted 200 pixels to the left

down = Actor("down")
down.pos = CENTER_X - 200, CENTER_Y + 230  # Shifted 200 pixels to the left

left = Actor("left")
left.pos = CENTER_X - 260, CENTER_Y + 170  # Shifted 200 pixels to the left


# Second player
dancer2 = Actor("dancer-start2")
dancer2.pos = CENTER_X + 70, CENTER_Y - 40 

up2 = Actor("up")
up2.pos = CENTER_X + 200, CENTER_Y + 110  # Shifted 200 pixels to the right

right2 = Actor("right")
right2.pos = CENTER_X + 260, CENTER_Y + 170  # Shifted 200 pixels to the right

down2 = Actor("down")
down2.pos = CENTER_X + 200, CENTER_Y + 230  # Shifted 200 pixels to the right

left2 = Actor("left")
left2.pos = CENTER_X + 140, CENTER_Y + 170  # Shifted 200 pixels to the right

score2 = 0
current_move2 = 0
move_list2 = []
game_over2 = False

def reset_dancer():
    global game_over
    if not game_over:
        dancer.image = "dancer-start"
        up.image = "up"
        right.image = "right"
        down.image = "down"
        left.image = "left"
    return

def reset_dancer2():
    global game_over2
    if not game_over2:
        dancer2.image = "dancer-start2"
        up2.image = "up"
        right2.image = "right"
        down2.image = "down"
        left2.image = "left"
    return

def update_dancer(move):
    global game_over
    if not game_over:
        if move == 0:
            up.image = "up-lit"
            dancer.image = "dancer-up"
            clock.schedule(reset_dancer, 0.5)
        elif move == 1:
            right.image = "right-lit"
            dancer.image = "dancer-right"
            clock.schedule(reset_dancer,0.5)
        elif move == 2:
            down.image = "down-lit"
            dancer.image = "dancer-down"
            clock.schedule(reset_dancer,0.5)
        else:
            left.image = "left-lit"
            dancer.image = "dancer-left"
            clock.schedule(reset_dancer,0.5)
    return

def update_dancer2(move):
    global game_over2
    if not game_over2:
        if move == 0:
            up2.image = "up-lit"
            dancer2.image = "dancer-up2"
            clock.schedule(reset_dancer2, 0.5)
        elif move == 1:
            right2.image = "right-lit"
            dancer2.image = "dancer-right2"
            clock.schedule(reset_dancer2,0.5)
        elif move == 2:
            down2.image = "down-lit"
            dancer2.image = "dancer-down2"
            clock.schedule(reset_dancer2,0.5)
        else:
            left2.image = "left-lit"
            dancer2.image = "dancer-left2"
            clock.schedule(reset_dancer2,0.5)
    return

def display_moves():
    global move_list, display_list, dance_length
    global say_dance, show_countdown, current_move
    if display_list:
        this_move = display_list[0]
        display_list = display_list[1:]
        if this_move == 0:
            update_dancer(0)
            update_dancer2(0)
            clock.schedule(display_moves, 1)
        elif this_move == 1:
            update_dancer(1)
            update_dancer2(1)
            clock.schedule(display_moves, 1)
        elif this_move == 2:
            update_dancer(2)
            update_dancer2(2)
            clock.schedule(display_moves, 1)
        else:
            update_dancer(3)
            update_dancer2(3)
            clock.schedule(display_moves, 1)
    else:
        say_dance = True
        show_countdown = False
    return

def generate_moves():
    global move_list, dance_length, count
    global show_countdown, say_dance
    count = 4
    move_list = []
    say_dance = False
    for move in range(0, dance_length):
        rand_move = randint(0, 3)
        move_list.append(rand_move)
        display_list.append(rand_move)
    show_countdown = True
    countdown()
    return

def countdown():
    global count, game_over, show_countdown
    if count > 1:
        count = count - 1
        clock.schedule(countdown, 1)
    else:
        show_countdown = False
        display_moves()
    return


def next_move():
    global dance_length, current_move, moves_complete
    if current_move < dance_length - 1:
        current_move = current_move + 1
    else:
        moves_complete = True
    return

def next_move2():
    global dance_length, current_move2, moves_complete
    if current_move2 < dance_length - 1:
        current_move2 = current_move2 + 1
    else:
        moves_complete = True
    return

def on_key_up(key):
    global score, game_over, move_list, current_move
    global score2, game_over2, move_list2, current_move2
    if key == keys.UP:
        update_dancer(0)
        if move_list[current_move] == 0:
            score = score + 1
            next_move()
        else:
            game_over = True
    elif key == keys.RIGHT:
        update_dancer(1)
        if move_list[current_move] == 1:
            score = score + 1
            next_move()
        else:
            game_over = True
    elif key == keys.DOWN:
        update_dancer(2)
        if move_list[current_move] == 2:
            score = score + 1
            next_move()
        else:
            game_over = True
    elif key == keys.LEFT:
        update_dancer(3)
        if move_list[current_move] == 3:
            score = score + 1
            next_move()
        else:
            game_over = True
    # Second player
    if key == keys.W:
        update_dancer2(0)
        if move_list[current_move2] == 0:
            score2 = score2 + 1
            next_move2()
        else:
            game_over2 = True
    elif key == keys.D:
        update_dancer2(1)
        if move_list[current_move2] == 1:
            score2 = score2 + 1
            next_move2()
        else:
            game_over2 = True
    elif key == keys.S:
        update_dancer2(2)
        if move_list[current_move2] == 2:
            score2 = score2 + 1
            next_move2()
        else:
            game_over2 = True
    elif key == keys.A:
        update_dancer2(3)
        if move_list[current_move2] == 3:
            score2 = score2 + 1
            next_move2()
        else:
            game_over2 = True
    
    if game_over or game_over2:
      if key == keys.SPACE:
          restart()
    return

generate_moves()
music.play(selected_music)

def update():
    global game_over, current_move, moves_complete
    global game_over2, current_move2  # Second player
    if not game_over and not game_over2:
        if moves_complete:
            generate_moves()
            moves_complete = False
            current_move = 0
            current_move2 = 0
    else:
        music.stop()
        
def draw():
    global game_over, score, say_dance
    global game_over2, score2  # Second player
    global count, show_countdown
    if not game_over:
        screen.clear()
        screen.blit("stage", (0, 0))
        dancer.draw()
        up.draw()
        down.draw()
        right.draw()
        left.draw()
        screen.draw.text("Score: " +
                         str (score), color="black",
                         topleft =(10, 10))
    # Second player
        dancer2.draw()
        up2.draw()
        down2.draw()
        right2.draw()
        left2.draw()
        screen.draw.text("Score2: " +
                         str(score2), color="black",
                         topleft=(10, 40))  # Change the position slightly
        if say_dance:
            screen.draw.text("Dance!", color="black", topleft=(CENTER_X - 8, 150), fontsize=60)
        if show_countdown:
            screen.draw.text(str(count), color="black", topleft=(CENTER_X -8, 150), fontsize=60)
    else:
        screen.clear()
        screen.blit("stage", (0, 0))
        screen.draw.text("Score: " +
                         str(score), color="black",
                         topleft=(10, 10))
        screen.draw.text("GAME OVER!", color="black",
                         topleft=(CENTER_X - 130, 220), fontsize=60)
    return

def restart():
    global score, current_move, moves_complete, game_over
    global score2, current_move2, game_over2  # Second player

    score = 0
    score2 = 0
    current_move = 0
    current_move2 = 0
    moves_complete = False
    game_over = False
    game_over2 = False

    # Randomly select a music file
    selected_music = random.choice(music_files)
    # Play the selected music file
    music.play(selected_music)

    generate_moves()

pgzrun.go()