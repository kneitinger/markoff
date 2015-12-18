try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A simple phrase generating class using Markov chains',
    'author': 'Kyle J. Kneitinger',
    'url': 'https://github.com/kneitinger/markoff',
    'author_email': 'kneit@pdx.edu',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['markoff','tests'],
    'scripts': [],
    'name': 'markoff'
    'license' : 'MIT',
    'classifiers' : [
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ],
}

setup(**config)
