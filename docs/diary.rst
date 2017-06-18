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

Started making the new theme. First, change ``conf.py`` to import the
theme and point at it. Missing a ``theme.conf`` so let's start there. This
then meant creating sphinx_bulma.css and sphinx_bulma.support.SphinxBulma
all as clones from alabaster.

Took sphinx/themes/basic/layout.html and copied it into sphinx_bulma's
templates directory as basic_layout.html.  This is the primary file that
will be converted to Bulma.

Before converting to Bulma, let's improve the workflow using the
``livereload`` package from PyPI, which has Sphinx auto-run integration.
This also means having a dev-requirements.txt package, to hold the
livereload requirements.

Made a basic src/sphinx_bulma/sphinx_bulma_base.scss which imported
everything and did no substituting. Need to get it included, so for now,
just did an @import on the first line in css_t.

