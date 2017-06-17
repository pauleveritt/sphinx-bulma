=================
Development Diary
=================

Notes as I go through the development.

I made a ``setup.py`` based on the recommendations in Hynek's post at
https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
and his ``attrs`` project.

Used PyCharm to generate sphinx quickstart. I then replaced the
``docs/conf.py`` settings that related to project name, version, etc. with
the values in ``src/sphinx_bulma/__init__.py`` that follow Hynek's approach.
