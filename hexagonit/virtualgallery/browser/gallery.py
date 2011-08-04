# -*- coding: utf-8 -*-
"""Render and display the Virtual 3D gallery."""
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class VirtualGalleryView(BrowserView):
    """A BrowserView to display the Virtual 3D gallery."""
    template = ViewPageTemplateFile('gallery.pt')

    def __call__(self):
        self.context_url = self.context.absolute_url()
        self.portal_url = self.context.portal_url()
        return self.template()

