from hexagonit.virtualgallery.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')

    def test_is_hexagonit_virtualgallery_installed(self):
        self.failUnless(self.installer.isProductInstalled('hexagonit.virtualgallery'))

    def test_uninstall(self):
        self.installer.uninstallProducts(['hexagonit.virtualgallery'])
        self.failIf(self.installer.isProductInstalled('hexagonit.virtualgallery'))

    def test_browserlayer(self):
        from hexagonit.virtualgallery.browser.interfaces import IHexagonitVirtualgalleryLayer
        from plone.browserlayer import utils
        self.failUnless(IHexagonitVirtualgalleryLayer in utils.registered_layers())
