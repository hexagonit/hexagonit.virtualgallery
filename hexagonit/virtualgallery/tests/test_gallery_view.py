# -*- coding: utf-8 -*-
"""Tests for @@virtualgallery view that renders out Virtual 3D gallery."""

import transaction

import unittest2 as unittest

from DateTime import DateTime

from zope.component import getUtility
from zope.interface import alsoProvides
from zope.interface.verify import verifyObject
from zope.testbrowser.interfaces import ILink
from plone.testing.z2 import Browser

from hexagonit.virtualgallery.tests.base import IntegrationTestCase


class TestView(IntegrationTestCase):
    """Test @@virtualgallery's view parameters."""

    def setUp(self):
        """Custom shared utility setup for tests."""

        # Prepare the request object
        from hexagonit.virtualgallery.browser.interfaces import IHexagonitVirtualgalleryLayer
        alsoProvides(self.layer['app'].REQUEST, IHexagonitVirtualgalleryLayer)
        self.layer['app'].REQUEST['ACTUAL_URL'] = self.layer['app'].REQUEST['URL']

        # Shortcuts
        self.portal = self.layer['portal']
        self.folder = self.portal.folder
        self.view = self.portal.folder.unrestrictedTraverse('virtualgallery')

    def test_galleryinit_urls(self):
        """Test if urls in galleryinit JavaScript are correct."""
        html = self.view()
        self.assertTrue('src="http://nohost/plone/++resource++hexagonit.virtualgallery/swfobject.js"' in html)
        self.assertTrue('dataURL:"http://nohost/plone/folder/@@virtualgallery.json"' in html)
        self.assertTrue('http://nohost/plone/++resource++hexagonit.virtualgallery/Virtual3DGallery.swf' in html)
        self.assertTrue('http://nohost/plone/++resource++hexagonit.virtualgallery/expressInstall.swf' in html)


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

