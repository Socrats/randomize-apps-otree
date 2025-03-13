"""
Copyright 2025 Elias Fernández Domingos

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from typing import List

from otree.api import *

from randomize_apps_api.api import *

from random import shuffle

doc = """
Creates randomized list of apps for each participant based on the apps_sequence of the session.
"""


class C(BaseConstants):
    NAME_IN_URL = 'end_randomize_apps'

    # Default values that need to be set in the session config
    NUM_ROUNDS = 1

    # You can edit this in case you want to randomize apps for groups of participants
    PLAYERS_PER_GROUP = None


## MODELS

class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
    pass


class Group(BaseGroup):
    pass


## PAGES

"""
Modify the is_displayed method and create different classes in case you want to apply a different
randomisation to different participants, according to your criteria.
"""


class RandomizeApps(RandomAppPage):
    @staticmethod
    def is_displayed(player):
        return True

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps: List[str]):
        # Only here to end the experiment
        return upcoming_apps


page_sequence = [RandomizeApps]
