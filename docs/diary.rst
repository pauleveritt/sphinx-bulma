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

For now, scrap this work. Instead of making alabaster_bulma, go back to
making a nice Bulma layout. Then, "port" to Jinja2/Sphinx/Alabaster.

nice_bulma_layout
=================

The
`Hero template <https://dansup.github.io/bulma-templates/templates/hero.html>`_
has a nice home page layout, with the splash image I'm looking for.
Start with
`its HTML <https://github.com/dansup/bulma-templates/blob/gh-pages/templates/hero.html>`_.
When the browser is small and responsiveness kicks in, provide a small JS
to handle the button click.

header_template
===============

Time to convert the header to be a Sphinx-driven dynamic template. Iterate
over ``rellinks`` and make header nav entries. Add a "Home" in front and
point it and the logo to the ``master_doc``. Change the download thing
to the search box.

Went a bit farther than I should. Put in some (dumb) tests to see if we are
on the home page. If so, put in the hero and 3 columns. If not, put in
the page contents.

sphinx_assets
=============

Need to get the CSS and JS from Sphinx.

Refactor the SCSS. Put into own directory, get rid (for now) of the .css_t
and thus, change the .scss to be just sphinx_bulma.scss/css. Break it
into several sub files and use the SCSS to suck in the Sphinx CSS, rather
than issue extra web requests to get it. (Oops, can't, as the
Sphinx CSS is ``.css_t``. Have to revisit that later.

Refactor the main template to define is_home. Find some way to move all
of that home page stuff into its own template.
xx
