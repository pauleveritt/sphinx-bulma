:sb_type: article

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

logo-component
==============

Instead of one big global space of templates and variables, it would be
nice to do like modern FE and have directories for components, each with
the template/SCSS/JS/images that are needed. Sphinx and Jinja2 don't
really make this too easy, but we can try.

First, make a logo directory and move the jinja2 templating out of
the master layout template, into a logo/logo.html template. Get this into
the layout template "in some way". It would be nice to make this
encapsulated (the globalness of Sphinx is an irritant.) Jinja2 includes
look nice, but don't allow passing arguments and let the "component" have
access to the current scope, so no dice. Let's try import, but later,
we'll try to have a Python helper which means reg that renders.

Another nice thing about import: it is cached somewhat. Later, with reg,
we can have several flavors of caching.

Next, refactor the SCSS to be isolated in the logo/logo.scss file and
included into the master file. Ultimately, everything including
layout/layout.scss will be isolated, except perhaps a sphinx-bulma specific
_variables.scss.

Then, as an experiment in really going components, have a class that gets
instantiated. This significantly increases the weirdness and complexity and
rubs up against the ultimate use of reg, as it requires some sphinx event
hooks to be used:

- A .rst page can have a ``sb_type`` field that says what kind of page it is,
  e.g. an Article (later, the YAML thing)

- This lets it have a custom Article component: class that renders
  itself, selects the layout template to use, the template to render that
  page (which is a big thing, get rid of the in-Jinja if/else/else),
  SCSS, JS, images, etc.

- An on-startup Sphinx event is hooked to populate a registry of components of
  known components

- The Sphinx on-render event handler finds the right component and returns
  the template to use

- Also let the component dictate the layout to use, possibly the
  layout "component"

- Have a default "page" component that is used if there is no sb_type marker