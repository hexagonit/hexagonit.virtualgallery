from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

GALLERYINIT = """
jQuery(function () { 
var flashvars = {
    dataURL:"%(context_url)s/@@virtualgallery.json"
};
var params = {
    menu: "false",
    scale: "noScale",
    allowFullscreen: "true",
    allowScriptAccess: "always",
    bgcolor: "#FFFFFF"
};
var attributes = {
    id:"Virtual3DGallery"
};
function callbackFn(e) {
    $("#virtualgallery-wrapper").height($("#virtualgallery-wrapper").width() / 2.5);
}
swfobject.embedSWF(
"%(portal_url)s/++resource++hexagonit.virtualgallery/Virtual3DGallery.swf",
"altContent", "100%%", "100%%", "10.0.0",
"%(portal_url)s/++resource++hexagonit.virtualgallery/expressInstall.swf",
flashvars, params, attributes, callbackFn);
});
"""


class VirtualGalleryView(BrowserView):
    """A BrowserView to display the Virtual 3D gallery."""
    template = ViewPageTemplateFile('gallery.pt')

    def __call__(self):
        return self.template()

    def swfobject_url(self):
        return self.context.portal_url() + \
               "/++resource++hexagonit.virtualgallery/swfobject.js"

    def galleryinit(self):
        return GALLERYINIT % dict(
            context_url=self.context.absolute_url(),
            portal_url=self.context.portal_url(),
         )
