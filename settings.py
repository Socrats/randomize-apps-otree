from os import environ

SESSION_CONFIGS = [
    {
        'name': 'randomize_apps',
        'display_name': "Randomize Apps",
        'num_demo_participants': 4,
        'app_sequence': ['begin_randomize_apps_otree', 'test_app1', 'test_app2', 'test_app3', 'end_randomize_apps_otree'],
    },
    {
        'name': 'randomize_apps_with_wait_page',
        'display_name': "Randomize Apps with a WaitPage",
        'num_demo_participants': 4,
        'app_sequence': ['begin_randomize_apps_otree', 'test_app1', 'test_app2', 'test_app4',
                         'end_randomize_apps_otree'],
    },
    {
        'name': 'mix_randomize_apps',
        'display_name': "Randomize Apps only some apps",
        'num_demo_participants': 4,
        'app_sequence': ['begin_randomize_apps_otree', 'test_app1', 'test_app2', 'test_app3',
                         'end_randomize_apps_otree', 'test_app5'],
    }
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['randomized_app_sequence']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(name='demo',
         display_name='Demo Room'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

SECRET_KEY = environ.get('OTREE_SECRET_KEY')

INSTALLED_APPS = ['otree']
