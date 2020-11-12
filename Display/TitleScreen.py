'''
    File name: TitleScreen.py
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
    CheckBox, RadioButtons, Button, PopUpDialog, TimePicker, DatePicker, DropdownList, PopupMenu
import sys
from asciimatics.event import KeyboardEvent

class TitleScreen(Frame):
    def __init__(self, screen):
        super(TitleScreen, self).__init__(screen, 0,0 ,
                                        has_shadow=False,
                                        name="Title Screen")
        self.centre = (screen.width // 2, screen.height // 2)
        effects = [
            Stars(screen, (screen.width + screen.height) // 2, start_frame=0),
            Print(screen,
                  FigletText("Recipe API Assignment"),
                  self.centre[1] - 5),
            Print(screen,
                  FigletText("Louis Millette"),
                  self.centre[1] + 1),
            self._speak(screen, "Press (space) to continue or (q) to exit ", (self.centre[0]-27, self.centre[1] + 13), 0),
        ]
        for effect in effects:
            self.add_effect(effect)

    def _speak(self, screen, text, pos, start):
        return Print(
            screen,
            SpeechBubble(text),
            x=pos[0] + 4, y=pos[1] - 4,
            colour=Screen.COLOUR_CYAN)

    def process_event(self, event):
        if isinstance(event, KeyboardEvent):
            c = event.key_code
            if c == 32:
                raise NextScene()
            if c == 113:
                raise StopApplication('User Ended')
