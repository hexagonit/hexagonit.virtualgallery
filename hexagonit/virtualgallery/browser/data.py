from Products.CMFCore.utils import getToolByName
from plone.app.contentlisting.interfaces import IContentListing
from Products.Five.browser import BrowserView

import json


def jsonize(items):
    images = []
    for item in items:
        images.append(dict(
            url=item.getURL(),
            description=item.Description(),
            author=item.Creator(),
            title=item.Title(),
        ))
    return json.dumps({
        "ui": dict(
            next="next",
            prev="prev",
            forward="forward",
            backward="backward",
            left="left",
            right="right",
            anaglyph="anaglyph",
            fullscreen="fullscreen",
            loadingImg="loading image:",
            spaceToEnterRoom="press space to enter",
            spaceToCloseUp="press space to zoom in",
            enterRoom="You entering room no [x] of [y]",
            enterRoomToolTip="Enter [x] room",
            roomName="Room [x]",
        ),
        "settings": dict(
            anaglyphModeEnabled="true",
        ),
        "images": images,
    })


class FolderJSON(BrowserView):
    """A BrowserView to generate Virtual Gallery JSON data for folders."""

    def __call__(self):
        items = self.context.restrictedTraverse('@@folderListing')()
        self.context.RESPONSE.setHeader('Content-Type', 'application/json')
        return jsonize(items)


class TopicJSON(BrowserView):
    """A BrowserView to generate Virtual Gallery JSON data for collections."""

    def __call__(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        query = self.context.buildQuery()
        brains = catalog(query)
        items = IContentListing(brains)
        return jsonize(items)
