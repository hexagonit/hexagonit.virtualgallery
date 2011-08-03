from zope.interface import Interface


class IHexagonitVirtualgalleryLayer(Interface):
    """Marker interface for browserlayer."""


class IVirtualgalleryEnabled(Interface):
    """Add this marker interface to your content-type to enable display of
    virtual gallery.
    """
