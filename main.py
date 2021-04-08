import pygame
import sys
from game import Note, Player
from constants import WIDTH, HEIGHT, BLACK, WHITE, BLUE, GREEN, YELLOW, FPS


pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
delta_time = 0

game_over = False
game_started = True
p_color = WHITE

current_time = 0
button_press_time = 0
q_button_time = 0

player = Player()

while not game_over:

    if game_started:
        game_started = False
        pygame.mixer.music.load('sounds/clap.wav')

    pygame.mixer.music.rewind()
    p_color = WHITE

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                q_button_time = current_time
                # print(f'current time: {current_time}')
                # print(delta_time)
                Note.note_list.append(Note(BLUE, 1, current_time))

            if event.key == pygame.K_SPACE or event.key == pygame.MOUSEBUTTONDOWN:
                button_press_time = pygame.time.get_ticks()
                # print(f'current time: {button_press_time}')

                try:
                    if Note.note_list[0]:
                        hitPos = Note.note_list[0].pos[0]
                except IndexError:
                    hitPos = 0

                def check_hit(notePos):
                    if round(abs((player.pos[0]+(player.size[0]/2)) - notePos), 3) < 60:
                        if round(abs((player.pos[0]+(player.size[0]/2)) - notePos), 3) < 30:
                            if round(abs((player.pos[0]+(player.size[0]/2)) - notePos), 3) < 20:
                                pygame.mixer.music.play()
                                return 'Perfect!!'
                            return 'Great!'
                        return 'Okay'
                    elif 52 < round(abs((player.pos[0]+(player.size[0]/2)) - notePos), 3) < 120:
                        return 'Miss...'

                print(round(player.pos[0]+(player.size[0]/2) - hitPos, 3))
                print(check_hit(hitPos))
                if (check_hit(hitPos)) != 'Miss...':
                    p_color = BLUE

                    

    screen.fill(BLACK)

    pygame.draw.rect(screen, p_color, pygame.Rect(player.pos, player.size))

    try:
        for note in Note.note_list:
            if note.pos[0] > player.pos[0] - 120:
                note.pos[0] -= ((WIDTH/2/FPS*note.speed)+delta_time*2)*2
            else:
                Note.note_list.remove(note)
            # print(round(note.pos[0], 5))
            pygame.draw.rect(screen, BLUE, pygame.Rect([note.pos[0], note.pos[1]], note.size))


    except ZeroDivisionError:
        print('There was a 0 Division error. If this is the first frame, ignore')
        pass

    # except ValueError:
    #     print('There was a value error... likely trying to delete something from the note list')



    current_time = pygame.time.get_ticks()
    pygame.display.flip()
    delta_time = (clock.tick(FPS))/1000
    clock.tick(FPS)
    # print(current_time)
