from typing import Union, List, Any, Optional, TypeVar, Type
from otree.api import BasePlayer

Player = TypeVar("Player", bound=BasePlayer)


class RandomAppPage:
    round_number: int
    template_name: str
    timeout_seconds: int
    timer_text: str
    form_model: str
    form_fields: List[str]

    @staticmethod
    def live_method(player: Player, data):
        pass

    @staticmethod
    def get_form_fields(player: Player):
        pass

    @staticmethod
    def vars_for_template(player: Player):
        pass

    @staticmethod
    def js_vars(player: Player):
        pass

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        pass

    @staticmethod
    def is_displayed(player: Player):
        pass

    @staticmethod
    def error_message(player: Player, values):
        pass

    @staticmethod
    def get_timeout_seconds(player: Player):
        pass

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        pass
