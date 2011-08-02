from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class VirtualGalleryView(BrowserView):
    """A BrowserView to display the Virtual 3D gallery."""
    template = ViewPageTemplateFile('gallery.pt')

    def __call__(self):
        if 'json_data' in self.request.keys():
            return self.json_data()
        return self.template()
    
    def json_data(self):
        return "bar"
