from tkinter import *
import random

tk = Tk()
WIDTH = 500
HEIGHT = 400
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()
score = 0
score_text = canvas.create_text(60, 20, text="Score: 0", fill="white", font=('Helvetica', 14))

class Paddle():
    def __init__(self):
        self.width = 80
        self.height = 10
        self.x = WIDTH / 2
        self.y = HEIGHT - 30
        self.speed = 20
        self.id = canvas.create_rectangle(self.x - self.width/2, self.y - self.height/2,
                                          self.x + self.width/2, self.y + self.height/2,
                                          fill="blue")

    def move_left(self, event):
        if self.x - self.width/2 > 0:
            self.x -= self.speed
            canvas.move(self.id, -self.speed, 0)

    def move_right(self, event):
        if self.x + self.width/2 < WIDTH:
            self.x += self.speed
            canvas.move(self.id, self.speed, 0)

class Block():
    def __init__(self):
        self.size = 20
        self.x = random.randint(20, WIDTH - 20)
        self.y = 0
        

def spawn_block():
    blocks = []
    blocks.append(Block())
    tk.after(1000, spawn_block)


tk.bind("<Right>", Paddle.move_right)
tk.bind("<Right>", Paddle.move_right)

# if __name__ == '__main__':
#     pass

paddle = Paddle()

tk.mainloop()
