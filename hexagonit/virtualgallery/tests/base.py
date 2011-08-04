# -*- coding: utf-8 -*-
"""Base module for unittesting"""

import unittest2 as unittest

from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_ID
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import applyProfile
from plone.testing import z2
from Acquisition import aq_inner
from zope.component import getMultiAdapter
from zope.interface import alsoProvides


class HexagonitVirtualgalleryLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import hexagonit.virtualgallery
        import plone.app.contentlisting
        self.loadZCML(package=hexagonit.virtualgallery)
        self.loadZCML(package=plone.app.contentlisting)
        z2.installProduct(app, 'hexagonit.virtualgallery')

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        applyProfile(portal, 'hexagonit.virtualgallery:default')

        # Create test contemt
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)
        portal.invokeFactory('Folder', 'folder')
        portal.invokeFactory('Topic', 'collection')

        # Commit so that the test browser sees these objects
        portal.portal_catalog.clearFindAndRebuild()
        import transaction
        transaction.commit()

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'hexagonit.virtualgallery')


FIXTURE = HexagonitVirtualgalleryLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="HexagonitVirtualgalleryLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="HexagonitVirtualgalleryLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING

