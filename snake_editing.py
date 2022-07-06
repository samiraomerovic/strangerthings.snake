import pygame
import random
import user_input

pygame.init()

red = (200, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 102)
green = (0, 255, 0)
bright_red = (255, 0, 0)

dis_width = 1366
dis_height = 768

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Eleven\'s Eggo Extravaganza')

image = pygame.image.load(r'eleven-snake.png')
waffle = pygame.image.load(r'waffle-snake.png')
pygame.display.set_icon(waffle)
waffle = pygame. transform. scale(waffle, (30, 30))
bkg = pygame.image.load("background.jpeg")
bkg = pygame. transform. scale(bkg, (dis_width, dis_height))
input_user_rect = pygame.Rect(560,285,275,32)
input_pass_rect = pygame.Rect(560,350,275,32)

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bodoni 72", 30)
score_font = pygame.font.SysFont("bodoni 72", 40)
login_font = pygame.font.SysFont("bodoni 72", 40)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0,0])


def our_snake(snake_block, snake_list, direction):
    offsetx = 0
    offsety = 0
    if direction == "right":
        offsetx = -10
    if direction == "left":
        offsetx = 10
    if direction == "down":
        offsety = 10
    if direction == "up":
        offsety = -10
    for x in snake_list:
        if x == snake_list[-1]:
            dis.blit(image, [x[0], x[1], snake_block, snake_block])
        else:
            dis.blit(waffle, [x[0] + offsetx, x[1] + offsety, snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3.5, dis_height / 4])

def button(msg, x, y, w, h, ic, ac, msgx, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(dis, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "login":
                game_login()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "register":
                game_register()
            elif action == "return":
                game_intro()
    else:
        pygame.draw.rect(dis, ic, (x, y, w, 70))

    font_style = pygame.font.SysFont("bodoni 72", 25)
    mesg = font_style.render(msg, True, white)
    dis.blit(mesg, ((x + msgx), (y + (50 / 2))))

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        dis.fill(black)
        font_style = pygame.font.SysFont("bodoni 72", 70)
        mesg = font_style.render("Eleven's Eggo Extravaganza", True, red)
        dis.blit(mesg, [dis_width / 3.5, dis_height / 4])

        button("Login", 600, 300, 150, 70, red, bright_red, 50, "login")
        button("Register", 600, 400, 150, 70, red, bright_red, 40, "register")
        button("Quit", 600, 500, 150, 70, red, bright_red, 50, "quit")

        pygame.display.update()
        clock.tick(15)

def Your_username():
    value = login_font.render("Username: ", True, white)
    dis.blit(value, [400,285])

def Your_password():
    value = login_font.render("Password: ", True, white)
    dis.blit(value, [405,350])

def game_login():

    login = True

    inputbox = user_input.InputBox(560, 280, 300, 32, pygame, dis)
    inputbox2 = user_input.InputBox(560, 345, 300, 32, pygame, dis)

    while login:
        dis.fill(black)
        font_style = pygame.font.SysFont("bodoni 72", 70)
        mesg = font_style.render("Login", True, white)
        dis.blit(mesg, [dis_width / 2.25, dis_height / 5])

        font_style = pygame.font.SysFont("bodoni 72", 30)
        mesg = font_style.render("Please enter your login credentials", True, white)
        dis.blit(mesg, [dis_width / 2.75, dis_height / 3.5])


        button("Login", 700, 600, 150, 70, red, bright_red, 50, "login")
        button("Return", 500, 600, 150, 70, red, bright_red, 40, "return")

        Your_username()
        Your_password()

        inputbox.draw()
        inputbox2.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                inputbox.handle_event(event)
                inputbox2.handle_event(event)
                # inputbox.update()
                inputbox.draw()
                inputbox2.draw()
                pygame.display.flip()

        pygame.display.update()
        clock.tick(15)


def game_register():

    register = True

    while register:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        dis.fill(black)
        font_style = pygame.font.SysFont("bodoni 72", 70)
        mesg = font_style.render("Register", True, white)
        dis.blit(mesg, [dis_width / 2.3, dis_height / 5])

        font_style = pygame.font.SysFont("bodoni 72", 30)
        mesg = font_style.render("Please enter your information below", True, white)
        dis.blit(mesg, [dis_width / 2.75, dis_height / 3.5])

        pygame.draw.rect(dis, white, input_user_rect, 2)
        pygame.draw.rect(dis, white, input_pass_rect, 2)

        button("Register", 700, 600, 150, 70, red, bright_red, 40, "login")
        button("Return", 500, 600, 150, 70, red, bright_red, 40, "return")

        Your_username()
        Your_password()

        pygame.display.update()
        clock.tick(15)

def gameLoop():
    global snake_speed
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block - 300) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block - 300) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            message("Game Over! Press Q to Quit or C to Play Again", white)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x1_change > 0 and len(snake_List) > 1:
                        continue
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x1_change < 0 and len(snake_List) > 1:
                        continue
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    if y1_change > 0 and len(snake_List) > 1:
                        continue
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    if y1_change < 0 and len(snake_List) > 1:
                        continue
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.blit(bkg, (0, 0))
        dis.blit(waffle, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        direction = ""
        if x1_change > 0:
            direction = "right"
        if x1_change < 0:
            direction = "left"
        if y1_change < 0:
            direction = "up"
        if y1_change > 0:
            direction = "down"
        our_snake(snake_block, snake_List, direction)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if foodx in range(int(x1), int(x1) + 50) and foody in range(int(y1), int(y1) + 50):
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            snake_speed += 1

        clock.tick(snake_speed)


    pygame.quit()
    quit()

game_intro()
gameLoop()



