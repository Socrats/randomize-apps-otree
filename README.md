[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14763626.svg)](https://doi.org/10.5281/zenodo.14763626)

# Randomized App Sequencing for oTree

This module extends oTree to allow for **randomized app sequencing**, **wait pages**, and **partial app randomization**
in oTree >= 5.4.0.

## 🚀 Features

- **Support for Wait Pages**: Participants will wait on a wait page until `PLAYERS_PER_GROUP` reach that wait page
  through different randomly assigned apps.
- **Support for Mixed Randomization**: You can specify which apps should be randomized by placing them between
  `begin_randomize_apps_otree` and `end_randomize_apps_otree`.
- **Improved Page Index Handling**: `_increment_index_in_pages` has been overridden to iterate through all pages
  correctly, ensuring that the next app is selected even if it appears earlier in oTree’s internal page index.

## ✅ Integration with oTree

To integrate the `randomize-apps-otree` app into your oTree project, follow these steps:

1. **Add the App to Your Project:**
   Ensure that the `begin-randomize-apps-otree` and `end-randomize-apps-otree` app` are included in your oTree project
   directory.
2. **Add the API to Your Project:**
   You must also add the folder `randomize_apps_api`, this will allow you to import the `RandomizedAppPage`, as
   explained below.
3. **Update your Pages**
    * Every last page of your app, or which already overwrites the method `app_after_this_page`, must be a child of `RandomizedAppPage` and not `Page`.
    * See the section ["how to use"](#How-to-use)
4. **Update `settings.py`:**
    * **Make sure that the `begin-randomize-apps-otree` is the first app** in ever configuration of your
      `SESSION_CONFIGS` in your `settings.py` file.
    * The apps you want to randomize must be between the apps `begin-randomize-apps-otree` and
      `end-randomize-apps-otree`.
    * It is possible to define apps you don't want to randomize. **But, they must come after the apps that will be
      randomized**. Unfortunately, the other way around is not possible at the moment.
    * You **must** add `randomized_app_sequence` to your `PARTICIPANT_FIELDS`.
    * There are three example
      configurations in the next section.

## 🔧 Configuration Examples

Now, instead of using a single `randomize-app-otree`, there are two boundary apps:

- `begin_randomize_apps_otree`
- `end_randomize_apps_otree`

These markers define which apps in `app_sequence` should be randomized. Below are three example configurations:

### 1️⃣ **Randomizing All Apps**

```python
{
    'name': 'randomize_apps',
    'display_name': "Randomize Apps",
    'num_demo_participants': 4,
    'app_sequence': ['begin_randomize_apps_otree', 'test_app1', 'test_app2', 'test_app3', 'end_randomize_apps_otree'],
}
```

🔹All test apps inside the markers (`test_app1`, `test_app2`, `test_app3`) will be randomized.

-------

### 2️⃣ **Randomizing Apps with a Wait Page**

```python
{
    'name': 'randomize_apps_with_wait_page',
    'display_name': "Randomize Apps with a WaitPage",
    'num_demo_participants': 4,
    'app_sequence': ['begin_randomize_apps_otree', 'test_app1', 'test_app2', 'test_app4', 'end_randomize_apps_otree'],
}
```

🔹 `test_app4` Includes a Wait Page.

-------

### 3️⃣ **Partially Randomizing Apps**

```python
{
    'name': 'mix_randomize_apps',
    'display_name': "Randomize Only Some Apps",
    'num_demo_participants': 4,
    'app_sequence': ['begin_randomize_apps_otree', 'test_app1', 'test_app2', 'test_app3',
                     'end_randomize_apps_otree', 'test_app5'],
}
```

🔹 Only `test_app1`, `test_app2`, and `test_app3` will be randomized, while `test_app5` remains in a fixed position.

------

## 📝 Notes

* There are five test apps: `test_app1`, `test_app2`, `test_app3`, `test_app4`, and `test_app5`.
* The system ensures proper iteration through pages, even if the next app in the sequence appears earlier in oTree’s
  internal indexing.
* Wait pages are now supported, ensuring that participants wait until enough players reach the page before proceeding.

## How to use

1. Configure Session Settings: Ensure that the `app_sequence` in the session configuration includes the apps you want to
   randomize between the apps `begin-randomize-apps-otree` and `end-randomize-apps-otree`. The `begin-randomize-apps-otree` app should be the first app in the sequence.
2. You must use `RandomAppPage` instead of`Page` in every page that might exit an app (e.g, the past page of the app, or
   a page with an exiting condition). All you need to do is to import it with
   `from randomize_apps_api.api import RandomAppPage`.

3. Modify App Pages: In each app that you want to randomize, ensure that the last page or any page with a condition to
   exit the app includes the`app_after_this_page`method. This method should return the next app in the randomized
   sequence. For example:

```python
from typing import List
from randomize_apps_api.api import *


class SomePage(RandomAppPage):
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps: List[str]):
        try:
            upcoming_app = upcoming_apps[0]
        except IndexError:
            upcoming_app = upcoming_apps
        return upcoming_app
```

## Modify the randomisation

* If you need to adapt the randomisation mechanism, all you need to do is to modify the `randomize_apps` function in
  `begin_randomize_apps_otree/__init__.py`.
* If you would like to randomize per group of participants, then you might need to make some changes to the
  `C.PLAYERS_PER_GROUP` constant in `begin_randomize_apps_otree/__init__.py`, and add a WaitPage, so that participants are
  grouped in your desired way.
* **DO NOT** modify the name of the apps `begin_randomize_apps_otree` and `end_randomize_apps_otree`.

## Test

This repository comes with 3 test configurations so that you can see how the app works, and make any necessary
modifications to adapt it to your needs. All you need to do is run the otree development server with
``otree devserver``.

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

If you find this repository useful, please star it on Github, and cite it in your articles with BibTeX:

```TeX
@software{elias_fernandez_2025_14763626,
  author       = {Fernández Domingos, Elias},
  title        = {randomize-apps-otree: Randomized App Sequencing for oTree},
  month        = jan,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {v0.1.0},
  doi          = {10.5281/zenodo.14763626},
  url          = {https://doi.org/10.5281/zenodo.14763626},
}
```

or in text format:

```
Fernández Domingos, E. (2025). randomize-apps-otree: Randomized App Sequencing for oTree (v0.1.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.14763626
```
