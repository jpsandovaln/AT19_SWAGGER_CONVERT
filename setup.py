# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Convert and Recognition Studio",
    author_email="support@jala.university",
    url="",
    keywords=["Swagger", "Convert and Recognition Studio"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    &lt;b&gt;C&amp;R Studio&lt;/b&gt;. Is a simple, smart and elegant tool with a lot utilities to manipulate multimedia files that are used in daily life. This is the only Converter that has such a wide range of unit conversion utilities with very simple and easy to use interface.&lt;br&gt;&lt;hr&gt; &lt;ul&gt;   &lt;sub&gt;Developed for Jala University (2023) by:&lt;/sub&gt;   &lt;b&gt;&lt;h3&gt;AT19 Team - International&lt;/h3&gt;&lt;/b&gt;   &lt;li&gt;&amp;#127463&amp;#127476 Carolina Vacaflor Nina&lt;/li&gt;   &lt;li&gt;&amp;#127462&amp;#127479 Celeste Palet Arias&lt;/li&gt;   &lt;li&gt;&amp;#127463&amp;#127476 Daniel Villarroel Chanlopkova&lt;/li&gt;   &lt;li&gt;&amp;#127463&amp;#127476 David Garnica Morales&lt;/li&gt;   &lt;li&gt;&amp;#127463&amp;#127476 Denisse Cordoba Sanabria&lt;/li&gt;   &lt;li&gt;&amp;#127464&amp;#127476 Fabian Cabrejo Arias&lt;/li&gt;   &lt;li&gt;&amp;#127464&amp;#127476 Leonardo Pacheco Carrillo&lt;/li&gt;   &lt;li&gt;&amp;#127463&amp;#127476 Maria Mamani Cruz&lt;/li&gt;   &lt;li&gt;&amp;#127463&amp;#127476 Martin Alvarez Alcoreza&lt;/li&gt;   &lt;li&gt;&amp;#127462&amp;#127479 Rocio Morales&lt;/li&gt;   &lt;li&gt;&amp;#127463&amp;#127476 Roger Renjifo Tarquino&lt;/li&gt;   &lt;li&gt;&amp;#127463&amp;#127476 Selmi Muraña Cayo&lt;/li&gt;   &lt;li&gt;&amp;#127463&amp;#127476 Telma Rios Fernandez&lt;/li&gt;   &lt;br&gt;&lt;sub&gt;Under supervision of the Trainer:&lt;/sub&gt;   &lt;br&gt;Paolo Sandoval &lt;/ul&gt; &lt;hr&gt;
    """
)
