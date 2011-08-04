============================
Virtual 3D gallery for Plone
============================

`hexagonit.virtualgallery` is a Plone add-on that renders a Flash-based 3D virtual gallery.

* `Source code @ GitHub <http://github.com/hexagonit/hexagonit.virtualgallery>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/hexagonit.virtualgallery>`_
* `Sphinx docs @ ReadTheDocs <http://readthedocs.org/docs/hexagonitvirtualgallery>`_

Installation
============

To install `hexagonit.virtualgallery` you simply add ``hexagonit.virtualgallery`` to the list of eggs in your buildout, run buildout and restart Plone. Then, install `hexagonit.virtualgallery` using the Add-ons control panel.

Usage
=====

Basic usage
-----------

This package adds the `Virtual 3D gallery` display mode to Folder and Collection. So, go to any folder or collection that contains images and select ``Virtual 3D gallery`` from the display drop-down menu. That's it!

AJAX usage
----------

You might want to display the gallery somewhere else or possibly in a toolbarless new window. To keep all Plone stuff away from the virtual gallery use a URL like below to only get the title of the gallery and the Flash object that displays it::

    http://<path>/<to>/<your>/<gallery>/<folder>/virtualgallery?ajax_load=1&ajax_include_head=1

