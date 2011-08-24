from zope.i18nmessageid import MessageFactory

HexagonitVirtualgalleryMessageFactory = MessageFactory('hexagonit.virtualgallery')
#: Marker for using the original image scale.
ORIGINAL_SCALE = '__original__'


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
