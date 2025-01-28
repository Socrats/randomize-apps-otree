# randomize-apps-otree

This app provides a (temporal - and hacky) solution to enable the randomisation of oTree apps per participants in
oTree >= 5.4.0.

## Integration with oTree

To integrate the `randomize-apps-otree` app into your oTree project, follow these steps:

1. **Add the App to Your Project:**
   Ensure that the `randomize-apps-otree` app is included in your oTree project directory.
2. **Add the API to Your Project:**
   You must also add the folder `randomise_apps_api`, this will allow you to import the `RandomisedAppPage`, as
   explained below.
3. **Update `settings.py`:**
   Add `randomize-apps-otree` to the `SESSION_CONFIGS` in your `settings.py` file. You can configure the session
   settings as needed. Here is an example configuration:

   ```python
   SESSION_CONFIGS = [
    {
        'name': 'randomized_apps',
        'display_name': "Randomized Apps",
        'num_demo_participants': 4,
        'app_sequence': ['randomize-apps-otree', 'another_app', 'yet_another_app'],
    },
   ]
   ```

## How to use

1. Configure Session Settings: Ensure that the `app_sequence` in the session configuration includes the apps you want to
   randomize.The randomize - apps - otree app should be the first app in the sequence.
2. You must use `RandomAppPage` instead of`Page` in every page that might exit an app(e.g, the past page of the app, or
   a page with an exiting condition).All you need to do is to import it with
   `from randomise_apps_api.api import RandomAppPage`.

3. Modify App Pages: In each app that you want to randomize, ensure that the last page or any page with a condition to
   exit the app includes the`app_after_this_page`method. This method should return the next app in the randomized
   sequence. For example:

```python
from typing import List
from randomise_apps_api.api import *


class SomePage(RandomAppPage):
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps: List[str]):
        return upcoming_apps[-1]
```

## Modify the randomisation

* If you need to adapt the randomisation mechanism, all you need to do is to modify the `randomise_apps` function in
  `randomize-apps-otree/__init__.py`.
* If you would like to randomise per group of participants, then you might need to make some changes to the
  `C.PLAYERS_PER_GROUP` constant in `randomize-apps-otree/__init__.py`, and add a WaitPage, so that participants are
  grouped in your desired way.

## Test

This repository comes with a test configuration so that you can see how the app works, and make any necessary
modifications to adapt it to your needs. All you need to do is run the otree development server with
``otree devserver``. In the admin page you will be able to run the `Randomized Apps` demo experiment, which will lead
you through 3 pages in a randomised order with the names of `test_app1`, `test_app2`, `test_app3`. You should see that
the order is (at least with a probability of 1 - (1/6)) not the same for all participants.

**Important:** To be able to run the test you **must** set the `OTREE_ADMIN_PASSWORD` and `OTREE_SECRET_KEY`
environmental variables, or change them directly in the `settings.py` file. **DO NOT** commit these variables to a
public repository!

## Report issues

If you find any issue(s), please report it (them) on
the [issues page](https://github.com/Socrats/randomize-apps-otree/issues).
And feel free to make a pull request with any improvements you make (you'll appear as a collaborator on the repository
in this case).

Make sure to describe concisely what happened, and provide enough information to reproduce the issue.

## Acknowledgements

If you find this repository useful, please start it on Github, and cite it in your articles.