try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A simple phrase generating class using Markov chains',
    'author': 'Kyle J. Kneitinger',
    'url': 'https://github.com/kneitinger/markoff',
    'author_email': 'kneit@pdx.edu',
    'version': '0.1.2',
    'install_requires': ['nose'],
    'packages': ['markoff','tests'],
    'scripts': [],
    'name': 'markoff',
    'license' : 'BSD',
    'classifiers' : [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Text Processing :: Linguistic'
    ]
}

setup(**config)
