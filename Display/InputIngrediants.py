'''
    File name: InputIngrediants.py
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
from asciimatics.renderers import SpeechBubble, FigletText, Box
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.sprites import Arrow, Plot, Sam
from asciimatics.paths import Path
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication, \
    InvalidFields
from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, \
    CheckBox, RadioButtons, Button, PopUpDialog, TimePicker, DatePicker, DropdownList, PopupMenu, Widget
import sys
import pprint

from .PickRecipies import create_recipie_frames


class InputIngredients(Frame):
    def __init__(self, screen):
        super(InputIngredients, self).__init__(screen,
                                        int(screen.height * 2 // 3),
                                        int(screen.width * 2 // 3),
                                        has_shadow=True,
                                        data={
                                            'ingredients': ['onions, green pepers, turmeric'],
                                            'recipies': "5",
                                            'pantry': 0
                                        },
                                        name="Input Ingredients")
        layout = Layout([1, 18, 1])
        self.add_layout(layout)
        layout.add_widget(Label("Ingrediaent List"), 1)
        ingredient_list_widget = TextBox(5,
                                  label="Enter the ingredients you wish to find dishes for.  Separate them with a comma (onions, green pepers, turmeric, etc.):",
                                  name="ingredients",
                                  line_wrap=False,
                                  on_change=self._on_change)
        pantry_widget = RadioButtons([("Yes", 1),
                                    ("No", 0)],
                                    label="include the pantry basics such as water, salt, flour, etc.?",
                                    name="pantry",
                                    on_change=self._on_change)
        text_widget = Text(label="How many recipies would you like to see?",
                 name="recipies",
                 on_change=self._on_change,
                 validator="^[0-9]*$")
        layout.add_widget(ingredient_list_widget, 1)
        layout.add_widget(pantry_widget, 1)
        layout.add_widget(Divider(height=2), 1)
        layout.add_widget(text_widget, 1)
        layout.add_widget(Divider(height=2), 1)
        layout2 = Layout([1, 1, 1], fill_frame=True)
        self.add_layout(layout2)
        layout2.add_widget(Button("Quit", self._quit), 2)
        layout2.add_widget(Button("Continue", self._continue), 1)
        layout2.add_widget(Button("Back", self._continue), 0)
        self.fix()

    def _on_change(self):
        self.save()
        if self.data.get('ingredients'):
            self.screen.ingrediants = ''.join(self.data['ingredients'])
        if self.data.get('pantry'):
            self.screen.use_pantry = self.data['pantry']
        if self.data.get('recipies'):
            self.number_of_recipies = int(self.data['recipies'])

    def _quit(self):
        raise StopApplication("User requested exit")

    def _continue(self):
        # self.screen.ingrediants = self.screen.food.read_ingredients(self.screen.ingrediants)
        self.screen.recipes = self.screen.food.search_recipes_online(self.screen.ingrediants, self.screen.use_pantry, self.number_of_recipies)
        last_scene = self.screen._scenes[-1]
        self.screen._scenes = self.screen._scenes[:-1]
        self.screen._scenes += create_recipie_frames(self.screen)
        self.screen._scenes.append(last_scene)
        raise NextScene("recipe0")

    def _previous(self):
        raise NextScene("Title")
