from otree.lookup import get_min_idx_for_app, get_page_lookup
from otree.views import Page, WaitPage
from otree.views.abstract import InvalidAppError, db


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
        app_sequence = self.participant.vars.get('randomized_app_sequence', [])
        if current_app != "begin_randomize_apps_otree":
            current_app_index = app_sequence.index(current_app)
            if current_app_index == len(app_sequence) - 1:
                return "end_randomize_apps_otree"
            else:
                upcoming_apps = app_sequence[current_app_index + 1:]
        else:
            upcoming_apps = app_sequence

        app_to_skip_to = self.call_user_defined('app_after_this_page', upcoming_apps)
        if app_to_skip_to:
            if app_to_skip_to not in upcoming_apps:
                msg = f'"{app_to_skip_to}" is not in the upcoming_apps list'
                raise InvalidAppError(msg)
            return get_min_idx_for_app(self.participant._session_code, app_to_skip_to)

    def _increment_index_in_pages(self):
        # when is this not the case?
        participant = self.participant
        assert self._index_in_pages == participant._index_in_pages

        # we should allow a user to move beyond the last page if it's mturk
        # also in general maybe we should show the 'out of sequence' page

        # we skip any page that is a sequence page where is_displayed
        # evaluates to False to eliminate unnecessary redirection

        page_index_to_skip_to = self._get_next_page_index_if_skipping_apps()
        is_skipping_apps = bool(page_index_to_skip_to)

        ## MODIFIED HERE! now it iterates through all pages, since it's possible to return to a previous page
        for page_index in range(
                # go to max_page_index+2 because range() skips the last index,
                # and it's possible to go to max_page_index + 1 (OutOfRange)
                1,
                participant._max_page_index + 2,
        ):
            participant._index_in_pages = page_index
            if page_index == participant._max_page_index + 1:
                # break and go to OutOfRangeNotification
                break
            if is_skipping_apps and page_index == page_index_to_skip_to:
                break

            # scope, receive, send
            page = get_page_lookup(
                participant._session_code, page_index
            ).page_class.instantiate_without_request()

            page.set_attributes(self.participant)
            if not is_skipping_apps and page._is_displayed():
                break

            # if it's a wait page, record that they visited
            if isinstance(page, WaitPage):

                if page.group_by_arrival_time:
                    # keep looping
                    # if 1 participant can skip the page,
                    # then all other participants should skip it also,
                    # as described in the docs
                    # so there is no need to mark as complete.
                    continue

                # save the participant, because tally_unvisited
                # queries index_in_pages directly from the DB
                db.commit()

                is_last, someone_waiting = page._tally_unvisited()
                if is_last and someone_waiting:
                    page._run_aapa_and_notify(page._group_or_subsession)
