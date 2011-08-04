# -*- coding: utf-8 -*-
"""Tests for gallery JSON generation."""

import transaction

import unittest2 as unittest
import json

from DateTime import DateTime

from zope.component import getUtility
from zope.interface import alsoProvides
from zope.interface.verify import verifyObject
from zope.testbrowser.interfaces import ILink
from plone.testing.z2 import Browser

from hexagonit.virtualgallery.tests.base import IntegrationTestCase
from hexagonit.virtualgallery.browser.data import FolderJSON
from hexagonit.virtualgallery.browser.data import TopicJSON


class TestItems(IntegrationTestCase):
    """Test retrieving items that are then JSON-ized."""

    def setUp(self):
        """Custom shared utility setup for tests."""

        # Shortcuts
        self.request = self.layer['request']
        self.portal = self.layer['portal']
        self.folder = self.portal.folder

        # Prepare the request object
        from hexagonit.virtualgallery.browser.interfaces import IHexagonitVirtualgalleryLayer
        alsoProvides(self.request, IHexagonitVirtualgalleryLayer)
        self.request['ACTUAL_URL'] = self.request['URL']

        # Add test content
        self.portal.folder.invokeFactory('Document', 'page')
        self.portal.folder.invokeFactory('Image', 'image',
            title="image title",
            description="image description"
        )

    def test_json_response(self):
        """Test JSON response: paramters, content-type, etc."""
        view = self.portal.folder.unrestrictedTraverse('virtualgallery.json')
        output = view()
        params = json.loads(output)

        # test response content-type
        self.assertEquals('application/json', self.request.RESPONSE.getHeader('Content-Type'))

        # test gallery parameters
        self.assertEquals(params['settings']['anaglyphModeEnabled'], 'false')

    def test_folder_items(self):
        """Test items returned for Folder."""
        view = self.portal.folder.unrestrictedTraverse('virtualgallery.json')
        output = view()

        # Test that we have the correct view class (according to content-type)
        self.assertIsInstance(view, FolderJSON)

        # test we have image in items, but not page
        items = json.loads(output).get('images')
        self.assertEquals(1, len(items))
        self.assertEquals('image title', items[0]['title'])

    def test_folder_items(self):
        """Test items returned for Collection."""
        # create a test Collection
        criterion = self.portal.collection.addCriterion('Type', 'ATPortalTypeCriterion')
        criterion.setValue(['Image', 'Document'])

        # get view
        view = self.portal.collection.unrestrictedTraverse('virtualgallery.json')
        output = view()

        # Test that we have the correct view class (according to content-type)
        self.assertIsInstance(view, TopicJSON)

        # test we have image in items, but not page
        items = json.loads(output).get('images')
        self.assertEquals(1, len(items))
        self.assertEquals('image title', items[0]['title'])


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

