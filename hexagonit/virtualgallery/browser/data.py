# -*- coding: utf-8 -*-
"""Prepare JSON data that is used in Flash for rendering Virtual 3D gallery."""
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from hexagonit.virtualgallery import HexagonitVirtualgalleryMessageFactory as _
from hexagonit.virtualgallery import ORIGINAL_SCALE
from hexagonit.virtualgallery.interfaces import IVirtualGallerySettings
from itertools import ifilter
from plone.app.contentlisting.interfaces import IContentListing

import json
import logging

LOG = logging.getLogger('hexagonit.virtualgallery')


class JSONBase(BrowserView):
    """Base class for generating JSON data for virtual gallery."""

    def image_url(self, item, scale):
        """Returns an URL to the image at the desired scale.

        If the scale is not available, falls back to the original
        scale of the image.

        :param item: An image object reference
        :type item: `plone.app.contentlisting.interfaces.IContentListingObject`

        :param scale: An image scale identifier
        :type scale: str

        :rtype: str
        :return: Scaled image URL.
        """
        if scale == ORIGINAL_SCALE:
            return item.getURL()

        image = item.getObject()
        scales = image.restrictedTraverse('@@images')
        try:
            return scales.scale('image', scale=scale).url
        except AttributeError:
            # The configured scale is no longer recognized, fall back to the
            # original image size.
            LOG.warn('Image scale "{0}" not available for {1}'.format(scale, item.getPath()))
            return item.getURL()

    def jsonize(self, items):
        # Consult the TinyMCE configuration to determine which types are images.
        image_types = set(getToolByName(self.context, 'portal_tinymce').imageobjects.strip().splitlines())
        settings = IVirtualGallerySettings(self.context)

        images = []
        for item in ifilter(lambda o: o.Type() in image_types, items):
            images.append(dict(
                url=self.image_url(item, settings.image_scale),
                description=item.Description(),
                author=u' ',
                title=item.Title(),
            ))

        # set response and return
        self.request.RESPONSE.setHeader('Content-Type', 'application/json')
        return json.dumps({
            "ui": dict(
                anaglyph=self.context.translate(_(u"Anaglyph")),
                fullscreen=self.context.translate(_(u"Fullscreen")),
                loadingImg=self.context.translate(_(u"Loading image:")),
                enterRoom=self.context.translate(_(u"Entering room [x] of [y]")),
                enterRoomToolTip=self.context.translate(_(u"Click to enter room [x]")),
            ),
            "settings": dict(
                anaglyphModeEnabled="false",
            ),
            "images": images,
            }, indent=2, sort_keys=True)


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
