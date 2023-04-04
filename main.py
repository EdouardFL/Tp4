import arcade
import random

# Variables qui définissent la hauteur et la largeur de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Liste des couleurs possible pour les cercles et les rectangles
COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
          arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]

class Cercle():
    """Classe qui créer les objets cercle"""
    def __init__(self, x, y, rayon, change_x, change_y, color):
        # Méthode Init qui créer un nouveau object cercle, prend en compte les paramètres suivant:
        self.rayon = rayon
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

    def update(self):
        # Méthode qui update la position du cercle chaque frame
        # On ajoute le change_x et le change_y au coordonnées X et Y afin de faire bouger le cercle
        self.x += self.change_x
        self.y += self.change_y

        # Inverser la direction du changement X/Y du cercle lorsqu'il sort hors de l'écran
        if self.x < self.rayon:
            self.change_x *= -1

        if self.y < self.rayon:
            self.change_y *= -1

        if self.x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1

        if self.y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1

    def draw(self):
        # Méthode qui dessine le cercle
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

class Rectangle():
    def __init__(self, x, y, width, height, change_x, change_y, color, angle):
        # Méthode Init qui créer un nouveau object rectangle, prend en compte les paramètres suivant:
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color
        self.angle = angle

    def update(self):
        # Méthode qui update la position du rectangle chaque frame
        # On ajoute le change_x et le change_y au coordonnées X et Y afin de faire bouger le rectangle
        self.x += self.change_x
        self.y += self.change_y

        # Inverser la direction du changement X/Y du rectangle lorsqu'il sort hors de l'écran
        if self.x < self.width:
            self.change_x *= -1
            self.angle *= -1

        if self.y < self.height:
            self.change_y *= -1
            self.angle *= -1

        if self.x > SCREEN_WIDTH - self.width:
            self.change_x *= -1
            self.angle *= -1

        if self.y > SCREEN_HEIGHT - self.height:
            self.change_y *= -1
            self.angle *= -1

    def draw(self):
        # Méthode qui dessine le rectangle
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)

class MyGame(arcade.Window):
    """Classe qui représente le jeu. Inhérite des méthodes d'une fenêtre arcade"""
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        # Méthode qui créer des listes
        # La liste_cercles contient tout les objects cercles
        # La liste_rectangles contient tout les objects rectangles
        self.liste_cercles = []
        self.liste_rectangles = []

    def on_draw(self):
        # Méthode d'arcade qui est activé chaque frame
        arcade.start_render()

        for cercle in self.liste_cercles:
            # Active les méthodes update et draw de chaque cercle dans la liste des cercles
            cercle.update()
            cercle.draw()

        for rectangle in self.liste_rectangles:
            # Active les méthodes update et draw de chaque rectangle dans la liste des rectangles
            rectangle.update()
            rectangle.draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Méthode d'arcade qui est activé a chaque fois que l'utilisateur click
        # Les paramètres X et Y représentes les coordonées du click
        # Le paramètre button représente le boutton de la sourie: 1 = click gauche et 4 = click droit
        if button == 1:
            # Si l'utilisateur fait un click gauche, on ajoute un nouveau objet cercle a liste des cercles
            rayon = random.randint(10, 30)
            center_x = x
            center_y = y
            change_x = random.randint(-10, 10)
            change_y = random.randint(-10, 10)
            color = random.choice(COLORS)
            cercleObject = Cercle(center_x, center_y, rayon, change_x, change_y, color)
            self.liste_cercles.append(cercleObject)

        elif button == 4:
            # Si l'utilisateur fait un click droit, on ajoute un nouveau objet rectangle a liste des rectangles
            width = random.randint(10, 60)
            height = random.randint(10, 60)
            center_x = x
            center_y = y
            change_x = random.randint(-10, 10)
            change_y = random.randint(-10, 10)
            color = random.choice(COLORS)
            angle = random.randint(-360,360)
            rectangleObject = Rectangle(center_x, center_y, width, height, change_x, change_y, color, angle)
            self.liste_rectangles.append(rectangleObject)

def main():
    # Fonction qui créer un nouveau objet jeu et fait le setup
    MyGame()

    arcade.run()

# On active la fonction main afin de commencer le jeu
main()
