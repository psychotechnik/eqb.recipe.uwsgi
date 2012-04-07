from setuptools import setup, find_packages

version = '0.0.2'

setup(
    name = "eqb.recipe.uwsgi",
    version = version,
    description = """\
            this is a recipe to build a uwsgi binary as well as the xml config file.
            modified version of https://github.com/shaunsephton/shaunsephton.recipe.uwsgi

    """,
    classifiers=[
    'Framework :: Buildout',
    'Topic :: Software Development :: Build Tools',
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    ],      
    #package_dir={'': 'eqb/recipe/uwsgi'},
    packages=find_packages(),
    keywords='buildout, uwsgi',
    author='Philip Kalinsky',
    author_email='philip.kalinsky@eloquentbits.com',
    url='https://github.com/psychotechnik/eqb.recipe.uwsgi',
    license='BSD',
    zip_safe=False,
    install_requires=[
        'zc.buildout',
    ],
    entry_points = {
        'zc.buildout': ['default = eqb.recipe.uwsgi:UWSGI']
    },
    )
