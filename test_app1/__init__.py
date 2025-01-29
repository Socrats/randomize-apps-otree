from otree.api import *

from randomize_apps_api.api import *


class C(BaseConstants):
    NAME_IN_URL = 'test_app1'

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
class Test1(RandomAppPage):

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        try:
            upcoming_app = upcoming_apps[0]
        except IndexError:
            upcoming_app = upcoming_apps
        return upcoming_app


page_sequence = [Test1]
