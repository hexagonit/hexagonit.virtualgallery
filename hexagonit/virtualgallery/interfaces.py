from hexagonit.virtualgallery import HexagonitVirtualgalleryMessageFactory as _
from hexagonit.virtualgallery import ORIGINAL_SCALE
from zope.interface import Interface
from zope.schema import Choice


class IVirtualGallerySettings(Interface):
    """Settings for a virtual gallery."""

    image_scale = Choice(
        title=_(u'label_image_scale', default=u'Image scale'),
        description=_(u'description_image_scale',
            default=u'Select the appropriate image scale to use in the '
                    u'virtual gallery. Using a smaller scale will make '
                    u'the gallery load faster but results in lesser quality '
                    u'images.'),
        vocabulary='hexagonit.virtualgallery.ImageScaleVocabulary',
        default=ORIGINAL_SCALE)
