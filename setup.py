from setuptools import setup

setup(
    name = "eqb.recipe.uwsgi",
    entry_points = {
        'zc.buildout': ['uwsgi = eqb.recipe.uwsgi:UWSGI']
    },
    )
