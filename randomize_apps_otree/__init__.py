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
    NAME_IN_URL = 'randomize_apps'

    # Default values that need to be set in the session config
    NUM_ROUNDS = 1

    # You can edit this in case you want to randomize apps for groups of participants
    PLAYERS_PER_GROUP = None


## MODELS - Modify them for your application if needed

class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    pass


class Player(BasePlayer):
    pass


class Group(BaseGroup):
    pass


## FUNCTIONS

def randomize_apps(apps_sequence: List[str]) -> None:
    """
    Randomize the sequence of apps per participant.

    The current behaviour is to shuffle the list of apps, and then proceed in order.
    If you want any other type of randomisation MODIFY this method.

    :param apps_sequence:
    :return: None
    """
    shuffle(apps_sequence)


## PAGES

"""
Modify the is_displayed method and create different classes in case you want to apply a different
randomisation to different participants, according to your criteria.
"""


class RandomizeApps(RandomAppPage):
    def is_displayed(self):
        return True

    @staticmethod
    def vars_for_template(player: Player):
        # First we copy app sequence from the session var into the participant var
        app_sequence = player.session.config['app_sequence']
        participant = player.participant

        # we remove the current app, as it should not be part of the randomisation
        # This is simple, since it MUST be the first app
        participant.vars['randomized_app_sequence'] = app_sequence[1:]

        # Now we randomize
        randomize_apps(participant.vars['randomized_app_sequence'])

        return {}

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps: List[str]):
        # IMPORTANT: add this to every last Page of each App which you want to randomize
        # This also applies to pages which have a condition to exit the app.
        return upcoming_apps[-1]


page_sequence = [RandomizeApps]
