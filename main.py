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

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_cercles = []

    def setup(self):
        # remplir la liste avec 20 objets de type Cercle
        for _ in range(20):
            rayon = random.randint(10, 30)
            center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLORS)
            cercleObject = Cercle(center_x, center_y, rayon, 5, 5, color)
            self.liste_cercles.append(cercleObject)

    def on_draw(self):
        arcade.start_render()

        for cercle in self.liste_cercles:
            cercle.update()
            cercle.draw()

        print("h")


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
