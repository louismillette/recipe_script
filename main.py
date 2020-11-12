#!/usr/bin/env python3

from asciimatics.scene import Scene
from asciimatics.screen import Screen
import sys

from Food.Food import Food
from Display.TitleScreen import TitleScreen
from Display.InputIngrediants import InputIngredients
from Display.PickRecipies import create_recipie_frames
from Display.ShoppingList import ShoppingList

import json

def play(screen):
    with open('groccery_list.txt', 'w') as write_file:
        write_file.write(json.dumps([]))
    scenes = []
    screen.ingrediants = []
    screen.use_pantry = True
    screen.number_of_recipies = 5
    screen.recipes = []
    screen.shopping_list = []
    screen.food = Food()
    scenes.append(Scene([
        TitleScreen(screen)
    ], -1, name="Title"))
    scenes.append(Scene([
        InputIngredients(screen)
    ], -1, name="Ingrediants")),
    scenes.append(Scene([
        ShoppingList(screen)
    ], -1, name="ShoppingList"))

    screen.play(scenes, stop_on_resize=True)

if __name__ == "__main__":
    Screen.wrapper(play)
