import pygame
import random
HEIGHT = 500
WIDTH = 900
LENGTH_PLAYER = 100
WIDTH_PLAYER = 10
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT]) # Set up the drawing window
state = "serve"
score1 = 0
score2 = 0
# player variables
y1 = 0
y2 = 0
yb = HEIGHT/2
x1 = 0 + 40
x2 = WIDTH - WIDTH_PLAYER -40
xb = WIDTH/2

font = pygame.font.Font('freesansbold.ttf', 40)
text = font.render(f"{score1}                       {score2}", True, "WHITE", "BLACK")
textRect = text.get_rect()
textRect.center = (WIDTH/2, 50)



def main():
    global y1, y2, x1, x2, yb, xb, xv, yv, state, ixv, iyv, text, textRect, score1, score2

    # Run until the user asks to quit
    running = True
    while running:
        # Did the user press any key or mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y1 = move_up(y1)

        elif keys[pygame.K_s]:
            y1 = move_down(y1)

        if keys[pygame.K_UP]:
            y2 = move_up(y2)


        elif keys[pygame.K_DOWN]:
            y2 = move_down(y2)

        elif keys[pygame.K_SPACE]:
            state = "play"

        if state == "play":
            move_ball()

        elif state == "serve":
            score()
            xb = WIDTH/2
            yb = HEIGHT/2
            ixv = random.choice([-5,5])
            iyv = random.choice([-5,5])
            xv = ixv
            yv = iyv



        # Fill the background with white
        screen.fill((0, 0, 0))

        draw_player(x1,y1)
        draw_player(x2,y2)
        screen.blit(text, textRect)
        draw_ball(xb, yb)
        score1, score2, state, text = end_game(score1, score2, state, text)




        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()



def draw_player(x,y):
    pygame.draw.rect(screen, "WHITE", pygame.Rect(x,y,WIDTH_PLAYER,LENGTH_PLAYER))

def draw_ball(xb, yb):
    pygame.draw.circle(screen, "WHITE", (xb,yb), 10)



def move_up(y):
    y -= 5
    if y <= 0:
        y = 0
    return y

def move_down(y):
    y += 5
    if y >= HEIGHT - LENGTH_PLAYER:
        y = HEIGHT - LENGTH_PLAYER
    return y

def move_ball():
    global xb, yb, xv,yv, y1, y2, x2, score1, score2, state

    xb += xv
    yb += yv
    #if xb <= 0 or xb >= WIDTH:
        #xv = xv*-1
    if yb <= 0 or yb >= HEIGHT:
        yv = yv*-1

    if (xb <= x1 + WIDTH_PLAYER and xb >= x1 and yb > y1 and yb < y1 + LENGTH_PLAYER/2) or (xb >= x2 - WIDTH_PLAYER and xb <= x2 and yb > y2 and yb < y2 + LENGTH_PLAYER/2):
        xv = xv * -1
        yv = -abs(yv)

    elif (xb <= x1 + WIDTH_PLAYER and xb >= x1 and yb >= y1 + LENGTH_PLAYER/2 and yb < y1 + LENGTH_PLAYER) or (xb >= x2 - WIDTH_PLAYER and xb <= x2 and yb >= y2 + LENGTH_PLAYER/2 and yb < y2 + LENGTH_PLAYER):
        xv = xv * -1
        yv = abs(yv)

    if xb <= 0 or xb >= WIDTH:
        state = "serve"



def score():
    global screen, score1, score2, xb, yb, text, font

    if xb <= 0:
        score2 += 1

    elif xb >= WIDTH:
        score1 += 1

    text = font.render(f"{score1}                       {score2}", True, "WHITE", "BLACK")

def end_game(score1, score2, state, text):


    if score1 == 5:
        return 0,0,"end",font.render("Player 1 WINS!!!", True, "WHITE", "BLACK")
    elif score2 == 5:
        return 0,0,"end",font.render("Player 2 WINS!!!", True, "WHITE", "BLACK")
    else:
        return score1, score2, state, text










if __name__ == "__main__":
    main()