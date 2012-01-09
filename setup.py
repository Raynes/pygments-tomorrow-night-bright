#!/usr/bin/python

from setuptools import setup

setup(
    name = 'pygments-style-tomorrow-night-bright',
    version = '0.1',
    description = 'Pygments version of the "Tomorrow Night" vim theme.',
    license = 'BSD',

    author = 'Byron Clark',
    author_email = 'byron@theclarkfamily.name',

    url = 'https://bitbucket.org/byronclark/pygments-style-tomorrow-night',

    packages = ['pygments_style_tomorrow_night_bright'],
    install_requires = ['pygments >= 1.4'],

    entry_points = '''[pygments.styles]
tomorrow-night-bright = pygments_style_tomorrow_night_bright:TomorrowNightBrightStyle''',

)
