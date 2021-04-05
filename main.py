import pygame
import sys
from rhythm import Note
from constants import WIDTH, HEIGHT, BLACK, WHITE, BLUE, GREEN, YELLOW, FPS


pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
game_over = False
game_started = True

current_time = 0
button_press_time = 0
q_button_time = 0

while not game_over:

    if game_started:
        game_started = False
        Note.note_list.append(Note(BLUE, 1, current_time))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                q_button_time = current_time
                print(f'current time: {current_time}')
                Note.note_list.append(Note(BLUE, 1, current_time))

            if event.key == pygame.K_SPACE or event.key ==pygame. MOUSEBUTTONDOWN:
                button_press_time = pygame.time.get_ticks()
                print(f'current time: {button_press_time}')

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, pygame.Rect([WIDTH / 2 - 25, HEIGHT / 1.25 - 25], [50, 50]))

    for note in Note.note_list:
        note.pos[0] -= ((WIDTH/2/note.speed)/FPS+note.speed/100)
        pygame.draw.rect(screen, BLUE, pygame.Rect([note.pos[0], note.pos[1]], note.size))

        if note.pos[0] < WIDTH/2-25:
            Note.note_list.remove(note)

#===============================================================================================
#===============================================================================================

#FIGURE OUT HOW TO MAKE THIS SHIT NOT MESS UP EVERY TIME THERE'S NO NOTES LEFT ON THE LIST


#ALSO TRY TO ADD THE SHIT TO SEND A NOTE AT A CERTAIN BPM, AND ALSO CALIBRATION

#===============================================================================================
#===============================================================================================
    if current_time - button_press_time < round(4000/FPS, 3):
        if current_time > q_button_time + Note.note_list[-1].speed*1000 and abs(q_button_time + Note.note_list[-1].speed*1000 - button_press_time) < round(3000/FPS, 3):
            screen.fill(GREEN)
        elif current_time > q_button_time + Note.note_list[-1].speed*1000 and abs(q_button_time + Note.note_list[-1].speed*1000 - button_press_time) < round(6000/FPS, 3):
            screen.fill(YELLOW)
        else:
            screen.fill(WHITE)


    current_time = pygame.time.get_ticks()
    pygame.display.flip()
    clock.tick(FPS)
    # print(current_time)
