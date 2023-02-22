import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
          arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]

class Cercle():
    def __init__(self, x, y, rayon, change_x, change_y, color):
        self.rayon = rayon
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

    def update(self):

        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.rayon:
            self.change_x *= -1

        if self.y < self.rayon:
            self.change_y *= -1

        if self.x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1

        if self.y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

class Rectangle():
    def __init__(self, x, y, width, height, change_x, change_y, color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

    def update(self):

        self.x += self.change_x
        self.y += self.change_y


        if self.x < self.width:
            self.change_x *= -1

        if self.y < self.height:
            self.change_y *= -1

        if self.x > SCREEN_WIDTH - self.width:
            self.change_x *= -1

        if self.y > SCREEN_HEIGHT - self.height:
            self.change_y *= -1

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_cercles = []
        self.liste_rectangles = []

    def setup(self):
        # remplir la liste avec 20 objets de type Cercle
        for _ in range(100):
            rayon = random.randint(10, 30)
            center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLORS)
            cercleObject = Cercle(center_x, center_y, rayon, random.randint(-10,10), random.randint(-10,10), color)
            self.liste_cercles.append(cercleObject)
        for _ in range(100):
            width = random.randint(10,60)
            height = random.randint(10,60)
            center_x = random.randint(0 + width, SCREEN_WIDTH - width)
            center_y = random.randint(0 + height, SCREEN_HEIGHT - height)
            color = random.choice(COLORS)
            rectangleObject = Rectangle(center_x, center_y, width, height, random.randint(-10,10), random.randint(-10,10), color)
            self.liste_rectangles.append(rectangleObject)

    def on_draw(self):
        arcade.start_render()

        for cercle in self.liste_cercles:
            cercle.update()
            cercle.draw()

        for rectangle in self.liste_rectangles:
            rectangle.update()
            rectangle.draw()

def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
