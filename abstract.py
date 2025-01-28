from otree.lookup import get_min_idx_for_app
from otree.views import Page
from otree.views.abstract import InvalidAppError


class RandomAppPage(Page):
    def _get_next_page_index_if_skipping_apps(self):
        # don't run it if the page is not displayed, because:
        # (1) it's consistent with other functions like before_next_page, vars_for_template
        # (2) then when we do
        #
        if not self._is_displayed():
            return
        if not hasattr(self, 'app_after_this_page'):
            return

        current_app = self.participant._current_app_name
        app_sequence = self.participant.vars.get('randomised_app_sequence', [])
        current_app_index = app_sequence.index(current_app)
        upcoming_apps = app_sequence[current_app_index + 1:]

        app_to_skip_to = self.call_user_defined('app_after_this_page', upcoming_apps)
        if app_to_skip_to:
            if app_to_skip_to not in upcoming_apps:
                msg = f'"{app_to_skip_to}" is not in the upcoming_apps list'
                raise InvalidAppError(msg)
            return get_min_idx_for_app(self.participant._session_code, app_to_skip_to)
