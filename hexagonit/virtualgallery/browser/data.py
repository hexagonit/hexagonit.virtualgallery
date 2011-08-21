# -*- coding: utf-8 -*-
"""Prepare JSON data that is used in Flash for rendering Virtual 3D gallery."""
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from hexagonit.virtualgallery import HexagonitVirtualgalleryMessageFactory as _
from plone.app.contentlisting.interfaces import IContentListing

import json


class JSONBase(BrowserView):
    """Base class for generating JSON data for virtual gallery."""

    def jsonize(self, items):
        # filter out non-image objects
        image_types = getToolByName(self.context, 'portal_tinymce').imageobjects
        items = [item for item in items if item.Type() in image_types]

        # construct list of images
        images = []
        for item in items:
            images.append(dict(
                url=item.getURL(),
                description=item.Description(),
                author=item.Creator(),
                title=item.Title(),
            ))

        # set response and return
        self.request.RESPONSE.setHeader('Content-Type', 'application/json')
        return json.dumps({
            "ui": dict(
                anaglyph="Anaglyph",
                fullscreen="Fullscreen",
                loadingImg="Loading image:",
                enterRoom="Entering room [x] of [y]",
                enterRoomToolTip="Click to enter",
            ),
            "settings": dict(
                anaglyphModeEnabled="false",
            ),
            "images": images,
        })


class FolderJSON(JSONBase):
    """A BrowserView to generate Virtual Gallery JSON data for folders."""

    def __call__(self):
        # get contents of this Folder
        items = self.context.restrictedTraverse('@@folderListing')()
        return self.jsonize(items)


class TopicJSON(JSONBase):
    """A BrowserView to generate Virtual Gallery JSON data for collections."""

    def __call__(self):
        # get result items of this Collection
        catalog = getToolByName(self.context, 'portal_catalog')
        query = self.context.buildQuery()
        brains = catalog(query)

        # convert catalog brains into plone.app.contentlisting items and return
        return self.jsonize(IContentListing(brains))
