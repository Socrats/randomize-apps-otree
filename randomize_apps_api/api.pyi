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
