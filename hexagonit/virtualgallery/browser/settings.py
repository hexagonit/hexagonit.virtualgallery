from BTrees.OOBTree import OOBTree
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from hexagonit.virtualgallery import HexagonitVirtualgalleryMessageFactory as _
from hexagonit.virtualgallery import ORIGINAL_SCALE
from hexagonit.virtualgallery.browser.interfaces import IVirtualgalleryEnabled
from hexagonit.virtualgallery.interfaces import IVirtualGallerySettings
from plone.app.imaging.utils import getAllowedSizes
from plone.app.z3cform.layout import wrap_form
from plone.memoize.view import memoize
from z3c.form import button
from z3c.form import field
from z3c.form import form
from zope.annotation.interfaces import IAnnotations
from zope.component import adapts
from zope.interface import implements
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


def ImageScaleVocabulary(context):
    """Vocabulary factory for available image scales.

    :param context: The context where the form using the vocabulary
        is being rendered.
    :type context: obj

    :rtype: zope.schema.vocabulary.SimpleVocabulary
    :return: A vocabulary of available image scales.
    """
    vocab = [(ORIGINAL_SCALE, _(u'Original size'))]
    # Get the available scales in descending order (based on the area)
    available_scales = sorted(
        getAllowedSizes().iteritems(),
        key=lambda s: s[1][0] * s[1][1],
        reverse=True)

    for scale, (width, height) in available_scales:
        vocab.append((scale, '{0} ({1}x{2})'.format(scale.title(), width, height)))

    return SimpleVocabulary([
        SimpleTerm(key, key, value) for key, value in vocab])


class GallerySettings(object):
    """Virtual gallery settings storage."""

    implements(IVirtualGallerySettings)
    adapts(IVirtualgalleryEnabled)

    def __init__(self, context):
        self.context = context
        self.storage = self._init_storage()

    def _init_storage(self):
        """Initializes the annotations for storing the settings."""
        ann = IAnnotations(self.context)
        if 'hexagonit.virtualgallery' not in ann:
            ann['hexagonit.virtualgallery'] = OOBTree()

        storage = ann['hexagonit.virtualgallery']
        if 'image_scale' not in storage:
            storage['image_scale'] = ORIGINAL_SCALE

        return storage

    @property
    def image_scale(self):
        return self.storage['image_scale']

    @image_scale.setter
    def image_scale(self, scale):
        self.storage['image_scale'] = scale


class SettingsForm(form.EditForm):
    """Form to edit virtualgallery settings."""

    fields = field.Fields(IVirtualGallerySettings)
    label = _(u'Virtual gallery settings')
    description = _('Configure this virtualgallery')

    @button.buttonAndHandler(_('Save changes'), name='save_changes')
    def handleApply(self, action):
        data, errors = self.extractData()

        if errors:
            self.status = _(u'Failed to update virtual gallery settings.')
            return

        self.applyChanges(data)
        self.status = _(u'Virtual gallery settings updated')


GallerySettingsForm = wrap_form(SettingsForm)


class GalleryEnabled(BrowserView):
    """Utility view to check gallery view status."""

    @memoize
    def __call__(self):
        """Checks if the virtual gallery view is currently enabled
        in the current context.

        :rtype: bool
        :returns: `True`, if virtual gallery view is active, `False`
            otherwise.
        """
        utils = getToolByName(self.context, 'plone_utils')
        try:
            return utils.browserDefault(self.context)[1][0] == "virtualgallery"
        except:
            return False
