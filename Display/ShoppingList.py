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
    CheckBox, RadioButtons, Button, PopUpDialog, TimePicker, DatePicker, DropdownList, PopupMenu
import sys
from asciimatics.event import KeyboardEvent
import json
import pprint

class ShoppingList(Frame):
    def __init__(self, screen):
        super(ShoppingList, self).__init__(screen,
                                        int(screen.height * 2 // 3),
                                        int(screen.width * 2 // 3),
                                        has_shadow=True,
                                        name="ShoppingList")
        self.drawn = False

    def initialize(self):
        self.drawn = True
        total_price = 0
        layout = Layout([1])
        self.add_layout(layout)
        layout.add_widget(Label('Shopping List', align='^', height=2), 0)
        layout.add_widget(Divider(height=1), 0)

        layout2 = Layout([1, 1, 1])
        self.add_layout(layout2)
        gorccery_list = self.screen.shopping_list
        layout2.add_widget(Label('Ingredient Name'), 0)
        layout2.add_widget(Label('Grocery Aisle'), 1)
        layout2.add_widget(Label('Price'), 2)
        for ingredient in gorccery_list:
            total_price += ingredient['price']
            layout2.add_widget(Label(f"   - {ingredient['name']}"), 0)
            layout2.add_widget(Label(f"   - {ingredient['aisle']}"), 1)
            layout2.add_widget(Label(f"{ingredient['price_display']}"), 2)
        layout2.add_widget(Divider(height=1))

        layout3 = Layout([1, 1, 1])
        self.add_layout(layout3)
        layout3.add_widget(Label(f"Total:"), 0)
        layout3.add_widget(Label(f"${round(total_price, 2)}", height=2), 2)

        layout4 = Layout([1])
        self.add_layout(layout4)
        layout4.add_widget(Label(f"Press Any Key to Exit", align='^'), 0)
        self.fix()

    def _speak(self, screen, text, pos):
        return Print(
            screen,
            SpeechBubble(text),
            x=pos[0] + 4, y=pos[1] - 4,
            colour=Screen.COLOUR_CYAN)

    def process_event(self, event):
        if isinstance(event, KeyboardEvent):
            raise StopApplication('User Ended')

    def _load_gorccery_list(self):
        with open('groccery_list.txt', 'r') as read_file:
            line = read_file.readline()
            list = json.loads(line)
        return list

    def update(self,frame):
        if not self.drawn:
            self.gorccery_list = self.screen.shopping_list
            self.initialize()
        super(ShoppingList, self).update(frame)
