"""Installation script for satchmo-colissimo
"""

from distutils.core import setup

setup(
    name = "satchmo-colissimo",
    packages = ["satchmo_colissimo"],
    version = "0.1",
    description = "satchmo-colissimo is a custom shipping module for satchmo, a django e-commerce solution.",
    author = "Julien Maupetit",
    author_email = "julien@maupetit.net",
    maintainer = "Julien Maupetit",
    maintainer_email = "julien@maupetit.net",
    url = "https://github.com/jmaupetit/satchmo-colissimo",
    download_url = "https://github.com/jmaupetit/satchmo-colissimo/zipball/master",
    keywords = ["django", "satchmo", "shipping", "colissimo", "la poste"],
    platforms = ["Platform independant",],
    classifiers = [        
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",        
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        ],
    license = "BSD",
    long_description = "".join( open('README.md').readlines() )
    )
