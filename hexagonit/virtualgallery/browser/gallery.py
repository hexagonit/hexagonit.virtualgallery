# -*- coding: utf-8 -*-
"""Render and display the Virtual 3D gallery."""
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class VirtualGalleryView(BrowserView):
    """A BrowserView to display the Virtual 3D gallery."""
    index = ViewPageTemplateFile('gallery.pt')

    def __call__(self):
        options = {
            'context_url': self.context.absolute_url(),
            'portal_url': self.context.portal_url()
        }
        return self.index(**options)
