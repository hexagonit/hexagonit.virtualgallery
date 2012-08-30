from setuptools import find_packages
from setuptools import setup
import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('hexagonit', 'virtualgallery', 'docs', 'README.rst') +
    read('hexagonit', 'virtualgallery', 'docs', 'FUTURE.rst') +
    read('hexagonit', 'virtualgallery', 'docs', 'CREDITS.rst') +
    read('hexagonit', 'virtualgallery', 'docs', 'HISTORY.rst') +
    read('hexagonit', 'virtualgallery', 'docs', 'LICENSE.rst'))


setup(
    name='hexagonit.virtualgallery',
    version='1.0',
    description="Virtual 3D image gallery for Plone",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Hexagon IT',
    author_email='oss@hexagonit.fi',
    url='http://hexagonit.fi/',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['hexagonit'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'hexagonit.testing',
        'plone.app.contentlisting',
        'plone.app.imaging',
        'plone.app.z3cform',
        'plone.browserlayer',
        'plone.memoize',
        'setuptools',
        'validictory',
        'zope.i18nmessageid'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
