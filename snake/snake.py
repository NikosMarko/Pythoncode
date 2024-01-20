from tkinter import *
import random



GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"



class MainMenu(Frame):
    pass
    def __init__(self):
        menu.__init__(self)



class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake"
            )
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        while check_wrong_spawn == False:
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
            print("wrong spawn")

        self.coordinates = [x, y]

        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food"
        )


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR
    )

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
        

    else:
        game.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


def check_wrong_spawn(snake, food):
    x, y = snake.coordinates[0]

    for x, y in snake.coordinates[0, 1]:
        if x == food.coordinates[0] and y == food.coordinates[1]:
            print("wrong")
            return False

    return True


def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False



def refresh_game():
    canvas.delete(ALL)

    global score, direction
    direction = "down"
    score = 0
    
    snake = Snake()
    food = Food()
    next_turn(snake, food)
    
    



def open_game():
    game = Toplevel()
    menu.destroy()
    
    

def open_menu():
    menu = Toplevel
    game.destroy()


def close_game():
    game.destroy()



def gameoverbuttons():

    playagain = Button(
    game,
    text="PLAY AGAIN",
    font=(40),
    bg="black",
    fg="green",
    command = refresh_game,
    borderwidth=1,
    )
    
    playagain.pack(fill="both", expand=True)
    playagain.place(x=((GAME_WIDTH // 2) - 200), y=(GAME_HEIGHT - 35))


    returnmenu = Button(
    game,
    text="MAIN MENU",
    font=(40),
    bg="black",
    fg="green",
    command = open_menu,
    borderwidth=1,
    )

    returnmenu.pack(fill="both", expand=True)
    returnmenu.place(x=((GAME_WIDTH // 2) - 50), y=(GAME_HEIGHT - 35))

    exitgame= Button(
    game,
    text="EXIT GAME",
    font=(40),
    bg="black",
    fg="green",
    command = close_game,
    borderwidth=1,
    )
    
    exitgame.pack(fill="both", expand=True)
    exitgame.place(x=((GAME_WIDTH // 2) + 110), y=(GAME_HEIGHT - 35))






def game_over():
    canvas.delete(ALL)
    canvas.create_text(
        canvas.winfo_width() / 2,
        canvas.winfo_height() / 2,
        font=("consolas", 70),
        text="GAME OVER",
        fill="red",
        tag="gameover",
    )
    gameoverbuttons()









menu = Tk()

menu.title("MAIN MENU")
menu.resizable(False, False)
menu.protocol("WM_DELETE_WINDOW", exit)

canvas = Canvas(menu, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


startBtn = Button(
    menu,
    text="Start game",
    font=(22),
    bg="black",
    fg="green",
    command = open_game,
    borderwidth=1,
)
startBtn.pack(fill="both", expand=True)
startBtn.place(x=((GAME_WIDTH // 2) - 50), y=(GAME_HEIGHT - 35))


menu.update()

menu_width = menu.winfo_width()
menu_height = menu.winfo_height()
screen_width = menu.winfo_screenwidth()
screen_height = menu.winfo_screenheight()

x = int((screen_width / 2) - (menu_width / 2))
y = int((screen_height / 2) - (menu_height / 2))

menu.geometry(f"{menu_width}x{menu_height}+{x}+{y}")


menu.mainloop()


game = Tk()
game.focus_force()
game.title("Snake")
game.resizable(False, False)


score = 0
direction = "down"

label = Label(game, text="Score:{}".format(score), font=("consolas", 40))
label.pack()

canvas = Canvas(game, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

game.update()

window_width = game.winfo_width()
window_height = game.winfo_height()
screen_width = game.winfo_screenwidth()
screen_height = game.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

game.geometry(f"{window_width}x{window_height}+{x}+{y}")

game.bind("<Left>", lambda event: change_direction("left"))
game.bind("<Right>", lambda event: change_direction("right"))
game.bind("<Up>", lambda event: change_direction("up"))
game.bind("<Down>", lambda event: change_direction("down"))

snake = Snake()
food = Food()

next_turn(snake, food)

game.mainloop()
