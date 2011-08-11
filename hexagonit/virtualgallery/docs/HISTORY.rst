Changelog
=========

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

