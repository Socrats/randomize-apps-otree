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

from otree.api import *

from randomize_apps_api.api import *


class C(BaseConstants):
    NAME_IN_URL = 'test_app5'

    # Default values that need to be set in the session config
    NUM_ROUNDS = 1

    # You can edit this in case you want to randomize apps for groups of participants
    PLAYERS_PER_GROUP = None


## Models

class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
    pass


class Group(BaseGroup):
    pass


## Pages
class Test5(RandomAppPage):
    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        try:
            upcoming_app = upcoming_apps[0]
        except IndexError:
            upcoming_app = upcoming_apps
        return upcoming_app


page_sequence = [Test5]
