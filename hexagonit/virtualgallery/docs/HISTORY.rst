Changelog
=========

1.0 (2011-08-26)
----------------

- Added support for configuring the image scale used in the gallery
  on per-context basis.
  [dokai]

- Updated documentation
  [dokai]

- Updated Finnish translations.
  [dokai]

- Support for translations added.
  [zupo]

- Fixed the Flash window mode so that Plone dropdown menus are visible
  on top of the Flash movie.
  [dokai]

- Updated the Flash movie to a new version. Highlights:

    * No more empty frames on walls.
    * The default position when entering a room shows the middle box
      with the room number better.
    * Redundant tooltips (prev, next, forward, backward, etc) removed.
    * Traversal through doors using mouse clicks.
    * Repositioned the prev/next and fullscreen buttons.
    * Fixed a bug with image info popups being sticky in fullscreen mode.
    * Fixed a bug with empty galleries.
    * Fixed a bug with tooltips not expanding correctly over different
      sized text.
    * Fixed a bug where in some cases clicking on an image would zoom-in
      on a wrong one.
    * Traversing through doors is possible with a single click.

  Removed also the now redundant entries in the JSON configuration.

  [dokai]

1.0b4 (2011-08-10)
------------------

- Really fix the packaging error. The setuptools ``unpack_tarfile`` function
  filters out symlinks when unpacking so they will not be present in the
  unpacked package. This, combined with some weirdness in either ``tar``
  itself or the Python tar module which reverses the order of the link,
  caused the targets of the symlinks to be removed from the final unpacked
  package.
  [dokai]

1.0b3 (2011-08-10)
------------------

- Fixed packaging error in 1.0b2.
  [dokai]

- JSON schema validation.
  [zupo]


1.0b2 (2011-08-04)
------------------

- Code cleanups.
  [zupo]

- More comments and documentation.
  [zupo]

- More tests.
  [zupo]


1.0b1 (2011-08-04)
------------------

- Initial release.
  [zupo]

