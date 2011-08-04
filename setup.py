from setuptools import find_packages
from setuptools import setup
import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


version = read('hexagonit', 'virtualgallery', 'version.txt').strip()

long_description = (
    read('hexagonit', 'virtualgallery', 'docs', 'README.rst') +
    read('hexagonit', 'virtualgallery', 'docs', 'FUTURE.rst') +
    read('hexagonit', 'virtualgallery', 'docs', 'CREDITS.rst') +
    read('hexagonit', 'virtualgallery', 'docs', 'HISTORY.rst') +
    read('hexagonit', 'virtualgallery', 'docs', 'LICENSE.rst'))


setup(name='hexagonit.virtualgallery',
      version=version,
      description="Virtual 3D image gallery for Plone",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Hexagon IT',
      author_email='oss@hexagonit.fi',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['hexagonit'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'manuel',
          'plone.app.contentlisting',
          'plone.app.testing',
          'plone.browserlayer',
          'setuptools',
          'unittest2',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
