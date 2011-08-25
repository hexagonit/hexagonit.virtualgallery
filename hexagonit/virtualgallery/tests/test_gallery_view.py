# -*- coding: utf-8 -*-
"""Tests for @@virtualgallery view that renders out Virtual 3D gallery."""
from hexagonit.virtualgallery.tests.base import IntegrationTestCase
from zope.annotation.attribute import AttributeAnnotations
from zope.interface import alsoProvides
from zope.publisher.browser import TestRequest

import mock
import unittest2 as unittest


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


class TestGalleryEnabled(unittest.TestCase):
    """Test the helper view which determines whether gallery is enabled."""

    def make_view(self, template_name=None, exception=None):
        """Creates a view instance bound to a mock context."""
        from hexagonit.virtualgallery.browser.settings import GalleryEnabled

        context = mock.Mock()
        if exception is not None:
            context.plone_utils.browserDefault.side_effect = exception

        context.plone_utils.browserDefault.return_value = (None, (template_name, ))

        return GalleryEnabled(context, TestRequest())

    @mock.patch('plone.memoize.view.IAnnotations', AttributeAnnotations)
    def test_gallery_enabled(self):
        view = self.make_view(template_name='virtualgallery')
        self.failUnless(view())

    @mock.patch('plone.memoize.view.IAnnotations', AttributeAnnotations)
    def test_gallery_disabled(self):
        view = self.make_view(template_name='some_other_template')
        self.failIf(view())

    @mock.patch('plone.memoize.view.IAnnotations', AttributeAnnotations)
    def test_error_fallback(self):
        view = self.make_view(exception=IndexError)
        self.failIf(view())


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
