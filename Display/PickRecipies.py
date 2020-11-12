'''
    File name: PickRecipies.py
    Author: Louis Millette
    Date created: 11/08/2020
    Date last modified: 11/12/2020
    Python Version: 3.6
'''

from __future__ import division
from builtins import range
import copy
import math
from asciimatics.effects import Cycle, Print, Stars
from asciimatics.renderers import SpeechBubble, FigletText, Box, ColourImageFile, FigletText, ImageFile
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.sprites import Arrow, Plot, Sam
from asciimatics.paths import Path
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication, \
    InvalidFields
from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, \
    CheckBox, RadioButtons, Button, PopUpDialog, TimePicker, DatePicker, DropdownList, PopupMenu
import sys

import requests
import shutil
import random
import string
import json
import os

def create_recipie_frames(screen):
    recipies,i = [],0
    for recipe in screen.recipes:
        recipies += [Scene([Recipie(screen, recipe)], -1,  name=f"recipe{i}")]
        i += 1
    return recipies

class Recipie(Frame):
    def __init__(self, screen, recipe):
        name = recipe['title']
        image_url = recipe['image']
        self.missed_ingredients = recipe['missedIngredients']
        self.recipie_id = recipe['id']
        used_ingredients = recipe['usedIngredients']
        super(Recipie, self).__init__(screen,
                                      int(screen.height) - 10,
                                      int(screen.width // 2),
                                      x=(int(screen.width // 2) - 5),
                                      has_shadow=True)
        layout = Layout([1])
        self.add_layout(layout)
        layout.add_widget(Label(name, align='^', height=2), 0)
        layout.add_widget(Divider(height=1), 0)

        layout2 = Layout([1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Label("Used Ingrediants", height=2), 0)
        for used_ingredient in used_ingredients:
            layout2.add_widget(Label(f"   - {used_ingredient['name']}"), 0)
        layout2.add_widget(Label("", height=1), 0)
        layout2.add_widget(Label("Ingrediants Required From the Groccery Store", height=2), 0)
        for missed_ingredient in self.missed_ingredients:
            layout2.add_widget(Label(f"   - {missed_ingredient['name']}"), 0)
        layout2.add_widget(Label("", height=1), 0)

        self.image_name = self._download_image(image_url)
        image = Print(screen, ColourImageFile(screen, self.image_name), x=5, y=5)
        self.add_effect(image)

        layout3 = Layout([1, 1, 1])
        self.add_layout(layout3)
        layout3.add_widget(Button("Don't Add And Continue", self._dont_add), 0)
        layout3.add_widget(Button("Add and Continue", self._add), 1)
        layout3.add_widget(Button("Quit", self._quit), 2)
        self.fix()

    def _download_image(self, image_url):
        if not os.path.exists('img'):
            os.makedirs('img')
        image_name = ''.join(random.choice(string.ascii_letters) for x in range(10))
        r = requests.get(image_url, stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(f'img/{image_name}', 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            print('Download Issues')
        return f'img/{image_name}'

    def _quit(self):
        shutil.rmtree('img')
        os.mkdir('img')
        raise StopApplication("User requested exit")

    def _add(self):
        self._delete_picture()
        self.screen.shopping_list += self.screen.food.add_prices_to_missed_ingredients(self.missed_ingredients, self.recipie_id)
        raise NextScene()

    def _dont_add(self):
        self._delete_picture()
        raise NextScene()

    def _delete_picture(self):
        os.remove(self.image_name)