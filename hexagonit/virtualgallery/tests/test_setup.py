# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from hexagonit.virtualgallery.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName
from zope.interface import alsoProvides
from zope.interface import providedBy

import unittest2 as unittest


class TestCase(IntegrationTestCase):
    """Test installation of hexagonit.virtualgallery into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_installed(self):
        """Test if hexagonit.virtualgallery is installed with
        portal_quickinstaller.
        """
        self.failUnless(self.installer.isProductInstalled('hexagonit.virtualgallery'))

    def test_uninstall(self):
        """Test if hexagonit.virtualgallery is cleanly uninstalled."""
        self.installer.uninstallProducts(['hexagonit.virtualgallery'])
        self.failIf(self.installer.isProductInstalled('hexagonit.virtualgallery'))

    # browser/configure.zcml
    def test_browserlayer(self):
        """Test that IHexagonitVirtualgalleryLayer is registered."""
        from hexagonit.virtualgallery.browser.interfaces import IHexagonitVirtualgalleryLayer
        from plone.browserlayer import utils
        self.failUnless(IHexagonitVirtualgalleryLayer in utils.registered_layers())

    # browser/configure.zcml
    def test_marker_interface(self):
        """Test that Folder and Collection provides IVirtualGalleryEnabled
        marker interface."""
        from hexagonit.virtualgallery.browser.interfaces import IVirtualgalleryEnabled
        self.assertTrue(IVirtualgalleryEnabled in providedBy(self.portal.folder))
        self.assertTrue(IVirtualgalleryEnabled in providedBy(self.portal.collection))

    # Folder.xml
    # Topic.xml
    def test_display_mode(self):
        """Test that the @@virtualgallery view is available in Folder's and
        Collection's display drop-down menu."""
        folder_views = self.portal.portal_types.Folder.view_methods
        collection_views = self.portal.portal_types.Topic.view_methods
        self.assertTrue('virtualgallery' in folder_views)
        self.assertTrue('virtualgallery' in collection_views)

        # test that default drop-down menu items are still there
        self.assertTrue('folder_summary_view' in folder_views)
        self.assertTrue('folder_full_view' in collection_views)


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

