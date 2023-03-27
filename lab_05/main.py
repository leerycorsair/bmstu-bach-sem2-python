#Программа предназначенна для изучения разработки анимаций на основе библиотеки PYGAME

#Леонов Владислав
#ИУ7-26Б

import pygame
from random import *
import math


def jump():
    global usr_y, make_jump, jump_counter
    if jump_counter >= -50:
        usr_y -= jump_counter // 2
        jump_counter -= 2
    else:
        jump_counter = 50
        make_jump = False


def draw_bird_l():
    global bird_x_l, bird_y_l, bird_height_r, bird_width_r, bird_mode_l, local_x_l, initial_y_l, bird_animation_l, b_l, score
    if bird_x_l <= display_width + bird_width_r:
        if bird_mode_l == 0:
            if b_l >= 50:
                b_l = 0
            display.blit(bird_animation_l[b_l // 10], (bird_x_l, bird_y_l))
            b_l += 1
            bird_x_l += randint(1,5)
        if bird_mode_l == 1:
            bird_y_l = int(math.sin(local_x_l) * 200) + initial_y_l
            local_x_l -= 0.05
            if b_l >= 50:
                b_l = 0
            display.blit(bird_animation_l[b_l // 10], (bird_x_l, bird_y_l))
            b_l += 1
            bird_x_l += randint(1,2)
    else:
        bird_x_l = -30
        bird_mode_l = randint(0, 1)
        b_l = 0
        score += 1
        if bird_mode_l == 0:
            bird_y_l = display_height - 200 + randint(-100, 100)
        elif bird_mode_l == 1:
            bird_y_l = (display_height - 100) // 2 + randint(-100, 100)
            initial_y_l = bird_y_l


def draw_bird_r():
    global bird_x_r, bird_y_r, bird_height_r, bird_width_r, bird_mode_r, local_x_r, initial_y_r, bird_animation_r, b_r, score
    if bird_x_r >= -bird_width_r:
        if bird_mode_r == 0:
            if b_r >= 50:
                b_r = 0
            display.blit(bird_animation_r[b_r // 10], (bird_x_r, bird_y_r))

            b_r += 1
            bird_x_r -= randint(1,5)
        if bird_mode_r == 1:
            bird_y_r = int(math.sin(local_x_r) * 200) + initial_y_r
            local_x_r -= 0.05
            if b_r >= 50:
                b_r = 0
            display.blit(bird_animation_r[b_r // 10], (bird_x_r, bird_y_r))
            b_r += 1
            bird_x_r -= randint(1,2)
    else:
        bird_x_r = display_width - 30
        bird_mode_r = randint(0, 1)
        b_r = 0
        score += 1
        if bird_mode_r == 0:
            bird_y_r = display_height - 200 + randint(-100, 100)
        elif bird_mode_r == 1:
            bird_y_r = (display_height - 100) // 2 + randint(-100, 100)
            initial_y_r = bird_y_r


def draw_character():
    global usr_x, usr_y, usr_animations_l, usr_animations_r, usr_animations_s, pos, l, r

    if pos == 'STAND':
        display.blit(usr_animations_s[0], (usr_x, usr_y))
    elif pos == 'LEFT':
        display.blit(usr_animations_l[l // 10], (usr_x, usr_y))
        l += 1
        if l > 80:
            l = 0
    elif pos == 'RIGHT':
        display.blit(usr_animations_r[r // 10], (usr_x, usr_y))
        r += 1
        if r > 80:
            r = 0

def collision():
    global usr_x, usr_y, usr_width, bird_y_r, bird_x_r, bird_width_r, bird_x_l, bird_y_l
    if (bird_x_r <= usr_x + 30 <= bird_x_r + bird_width_r) and (bird_y_r <= usr_y+30 <= bird_y_r + bird_height_r):
        return True
    if (bird_x_r <= usr_x + usr_width - 20 <= bird_x_r + bird_width_r) and (bird_y_r <= usr_y +30 <= bird_y_r + bird_height_r):
        return True
    if (bird_x_r <= usr_x + usr_width - 20 <= bird_x_r + bird_width_r) and (bird_y_r <= usr_y + usr_height +30 <= bird_y_r + bird_height_r):
        return True
    if (bird_x_r <= usr_x + 30 <= bird_x_r + bird_width_r) and (bird_y_r <= usr_y + 30 + usr_height <= bird_y_r + bird_height_r):
        return True
    if (bird_x_l <= usr_x + 30 <= bird_x_l + bird_width_r) and (bird_y_l <= usr_y+30 <= bird_y_l + bird_height_r):
        return True
    if (bird_x_l <= usr_x + usr_width - 20 <= bird_x_l + bird_width_r) and (bird_y_l <= usr_y +30 <= bird_y_l + bird_height_r):
        return True
    if (bird_x_l <= usr_x + usr_width - 20 <= bird_x_l + bird_width_r) and (bird_y_l <= usr_y + usr_height +30 <= bird_y_l + bird_height_r):
        return True
    if (bird_x_l <= usr_x + 30 <= bird_x_l + bird_width_r) and (bird_y_l <= usr_y + 30 + usr_height <= bird_y_l + bird_height_r):
        return True



def run_game():
    game = True
    global make_jump, usr_x, usr_y, usr_width, usr_height, pos, score
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            make_jump = True
        if make_jump:
            jump()
        if keys[pygame.K_LEFT]:
            if usr_x - 5 > -30:
                usr_x -= 5
            pos = 'LEFT'
        elif keys[pygame.K_RIGHT]:
            if usr_x + 5 < display_width - 100:
                usr_x += 5
            pos = 'RIGHT'
        else:
            pos = 'STAND'



        display.blit(pygame.image.load('background.jpg'), (0, 0))
        draw_bird_l()
        draw_bird_r()
        draw_character()
        print_text('Score: '+str(score), 0, 0)
        if collision():
            game = False
        pygame.display.update()
        clock.tick(100)


pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Summer Dodger')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

usr_animations_l = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
                    pygame.image.load('L4.png'),
                    pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'),
                    pygame.image.load('L8.png'),
                    pygame.image.load('L9.png')]
usr_animations_r = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
                    pygame.image.load('R4.png'),
                    pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'),
                    pygame.image.load('R8.png'),
                    pygame.image.load('R9.png')]

bird_animation_r = [pygame.image.load('BR0.png'), pygame.image.load('BR1.png'), pygame.image.load('BR2.png'),
                    pygame.image.load('BR3.png'), pygame.image.load('BR4.png'), pygame.image.load('BR5.png')]

bird_animation_l = [pygame.image.load('BL0.png'), pygame.image.load('BL1.png'), pygame.image.load('BL2.png'),
                    pygame.image.load('BL3.png'), pygame.image.load('BL4.png'), pygame.image.load('BL5.png')]

usr_animations_s = [pygame.image.load('standing.png')]
usr_width = 106
usr_height = 106
usr_x = display_width // 3
usr_y = display_height - 100 - usr_height
pos = 'STAND'
l = r = 0

clock = pygame.time.Clock()

make_jump = False
jump_counter = 50

bird_width_r = 104
bird_height_r = 50
bird_x_r = display_width - 30
bird_y_r = (display_height - 100) // 2 + randint(-100, 100)
bird_mode_r = randint(0, 1)
b_l = b_r = 0
local_x_r = 0
initial_y_r = bird_y_r

bird_x_l = - 30
bird_y_l = (display_height - 100) // 2 + randint(-100, 100)
bird_mode_l = randint(0, 1)
local_x_l = 0
initial_y_l = bird_y_l

score = 0
def print_text(message, x, y, font_color = (0, 0, 0), font_type = 'PingPong.ttf', font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x,y))

run_game()